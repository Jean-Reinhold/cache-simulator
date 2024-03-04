import random
from typing import Any, Optional


class ReplacementStrategy:
    def select_replacement_index(
        self,
        cache_set_index: int,
        cache_line: list[Optional[dict[str, Any]]],
    ) -> int:
        raise NotImplementedError("This method must be implemented in subclasses")

    def update_access(self, cache_set_index: int, slot: int):
        pass


class RandomReplacement(ReplacementStrategy):
    def select_replacement_index(
        self,
        cache_set_index: int,
        cache_line: list[Optional[dict[str, Any]]],
    ) -> int:
        empty_slots = [i for i, slot in enumerate(cache_line) if slot is None]
        if empty_slots:
            return random.choice(empty_slots)
        return random.randrange(len(cache_line))


class FIFOReplacement(ReplacementStrategy):
    def __init__(self):
        self.insertion_order = {}

    def select_replacement_index(
        self, cache_set_index: int, cache_line: list[Optional[dict[str, Any]]]
    ) -> int:
        empty_slots = [i for i, slot in enumerate(cache_line) if slot is None]
        if empty_slots:
            return empty_slots[0]
        if cache_set_index not in self.insertion_order:
            self.insertion_order[cache_set_index] = list(range(len(cache_line)))

        slot = self.insertion_order[cache_set_index].pop(0)
        self.insertion_order[cache_set_index].append(slot)
        return slot


class LRUReplacement(ReplacementStrategy):
    def __init__(self):
        self.access_order = {}

    def select_replacement_index(
        self, cache_set_index: int, cache_line: list[Optional[dict[str, Any]]]
    ) -> int:
        empty_slots = [i for i, slot in enumerate(cache_line) if slot is None]
        if empty_slots:
            if cache_set_index not in self.access_order:
                self.access_order[cache_set_index] = [0]
            self.update_access(cache_set_index, empty_slots[0])
            return empty_slots[0]

        if cache_set_index not in self.access_order:
            self.access_order[cache_set_index] = [0]

        lru_slot = self.access_order[cache_set_index].pop(0)
        self.access_order[cache_set_index].append(lru_slot)
        return lru_slot

    def update_access(self, cache_set_index: int, slot: int):
        if slot in self.access_order[cache_set_index]:
            self.access_order[cache_set_index].remove(slot)
        self.access_order[cache_set_index].append(slot)


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
