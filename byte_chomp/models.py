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
    compact_output: int = 1
    compulsory: int = 0
    capacity: int = 0
    conflict: int = 0
    hits: int = 0

    @property
    def total_misses(self):
        return self.compulsory + self.capacity + self.conflict

    @property
    def report(self):
        hit_rate = (
            self.hits / (self.hits + self.total_misses)
            if (self.hits + self.total_misses) > 0
            else 0
        )
        miss_rate = 1 - hit_rate
        compulsory_miss_rate = (
            self.compulsory / self.total_misses if self.total_misses > 0 else 0
        )
        capacity_miss_rate = (
            self.capacity / self.total_misses if self.total_misses > 0 else 0
        )
        conflict_miss_rate = (
            self.conflict / self.total_misses if self.total_misses > 0 else 0
        )
        if self.compact_output:
            report = [
                self.total_misses + self.hits,
                round(hit_rate, 4),
                round(miss_rate, 4),
                round(compulsory_miss_rate, 4),
                round(capacity_miss_rate, 4),
                round(conflict_miss_rate, 4),
            ]
            for i in report:
                print(i, end=" ")
            print("")

            return report

        report = {
            "requests": self.total_misses + self.hits,
            "hit_rate": round(hit_rate, 4),
            "miss_rate": round(miss_rate, 4),
            "compulsory": round(compulsory_miss_rate, 4),
            "capacity": round(capacity_miss_rate, 4),
            "conflict": round(conflict_miss_rate, 4),
        }
        print(report)
        return report


class CacheTable(BaseModel):
    num_sets: int
    associativity: int
    table: list[list[Optional[dict[str, Any]]]] = Field(default_factory=list)

    def __init__(self, **data):
        super().__init__(**data)
        self.table = [
            [None for _ in range(self.associativity)] for i in range(self.num_sets)
        ]

    def get_cache_line(self, index: int) -> list[Optional[dict[str, Any]]]:
        return self.table[index]

    def update_cache_line(self, index: int, slot: int, entry: dict[str, Any]) -> None:
        self.table[index][slot] = entry

    def find_tag_in_line(self, index: int, tag: int) -> tuple[bool, int]:
        cache_line = self.get_cache_line(index)
        for i, entry in enumerate(cache_line):
            if entry and entry["tag"] == tag:
                return True, i
        return False, -1

    def is_full(self) -> bool:
        return all([all(line) for line in self.table])
