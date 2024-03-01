from typing import Any, Optional
from pydantic import BaseModel, Field


class CacheConfig(BaseModel):
    n_sets: int
    b_size: int
    assoc: int
    pol: str
    output_flag: int
    filename: str


class CachePerformanceStats(BaseModel):
    compulsory: int = Field(0, description="Count of compulsory misses")
    capacity: int = Field(0, description="Count of capacity misses")
    conflict: int = Field(0, description="Count of conflict misses")
    hits: int = Field(0, description="Count of hits")

    def increment_error(self, error_type: str) -> None:
        if error_type == "Compulsory":
            self.compulsory += 1
        elif error_type == "Capacity":
            self.capacity += 1
        elif error_type == "Conflict":
            self.conflict += 1
        else:
            raise ValueError("Invalid error type")

    def increment_hit(self) -> None:
        self.hits += 1

    @property
    def total_misses(self):
        return self.compulsory + self.capacity + self.conflict


class AccessHistory(BaseModel):
    history: list[list[int]]

    def update_history(self, index: int, slot: int) -> None:
        self.history[index].remove(slot)
        self.history[index].append(slot)

    def get_next_slot(self, index: int) -> int:
        return self.history[index].pop(0)


class CacheTable:
    def __init__(self, num_sets: int, associativity: int):
        self.table: list[list[Optional[dict[str, Any]]]] = [
            [None for _ in range(associativity)] for _ in range(num_sets)
        ]

    def get_cache_line(self, set_index: int) -> list[Optional[dict[str, Any]]]:
        """Returns a specific cache line by set index."""
        return self.table[set_index]

    def update_cache_line(
        self, set_index: int, slot: int, entry: dict[str, Any]
    ) -> None:
        """Updates a specific slot in a cache line."""
        self.table[set_index][slot] = entry

    def find_tag_in_line(self, set_index: int, tag: int) -> tuple[bool, int]:
        for slot, entry in enumerate(self.table[set_index]):
            if entry is not None and entry["tag"] == tag:
                return True, slot
        return False, -1
