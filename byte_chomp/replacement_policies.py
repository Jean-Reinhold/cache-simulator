import random
from typing import Any, Optional
from pydantic import BaseModel

from byte_chomp.models import AccessHistory


class ReplacementStrategy(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    def select_replacement_index(
        self,
        cache_set_index: int,
        cache_line: list[Optional[dict[str, Any]]],
        access_history: AccessHistory,
    ) -> int:
        raise NotImplementedError("This method must be implemented in subclasses")

    def prepare(self, access_history: AccessHistory, set_associativity: int) -> None:
        pass


class RandomReplacement(ReplacementStrategy):
    def select_replacement_index(
        self,
        cache_set_index: int,
        cache_line: list[Optional[dict[str, Any]]],
        access_history: AccessHistory,
    ) -> int:
        return random.randrange(len(cache_line))


class FIFOReplacement(ReplacementStrategy):
    def prepare(self, access_history: AccessHistory, set_associativity: int) -> None:
        access_history.history = [
            list(range(set_associativity)) for _ in range(len(access_history.history))
        ]

    def select_replacement_index(
        self,
        cache_set_index: int,
        cache_line: list[Optional[dict[str, Any]]],
        access_history: AccessHistory,
    ) -> int:
        slot = access_history.get_next_slot(cache_set_index)
        access_history.update_history(cache_set_index, slot)
        return slot


class LRUReplacement(ReplacementStrategy):
    def prepare(self, access_history: AccessHistory, set_associativity: int) -> None:
        access_history.history = [
            list(range(set_associativity)) for _ in range(len(access_history.history))
        ]

    def select_replacement_index(
        self,
        cache_set_index: int,
        cache_line: list[Optional[dict[str, Any]]],
        access_history: AccessHistory,
    ) -> int:
        slot = next((i for i, entry in enumerate(cache_line) if entry is None), None)
        if slot is not None:
            return slot
        slot = access_history.get_next_slot(cache_set_index)
        access_history.update_history(cache_set_index, slot)
        return slot


def get_replacement_policy(policy_str: str):
    policy_map = {
        "R": RandomReplacement,
        "F": FIFOReplacement,
        "L": LRUReplacement,
    }
    policy_class = policy_map.get(policy_str)
    if policy_class:
        return policy_class()
    else:
        raise ValueError(f"Unknown replacement policy: {policy_str}")
