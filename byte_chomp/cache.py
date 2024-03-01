import math
from pydantic import BaseModel, ConfigDict

from byte_chomp.models import (
    CachePerformanceStats,
    AccessHistory,
    CacheTable,
    CacheConfig,
)
from byte_chomp.replacement_policies import ReplacementStrategy, get_replacement_policy


class Cache(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    num_sets: int
    block_size: int
    associativity: int
    replacement_policy: ReplacementStrategy
    cache_table: CacheTable
    access_history: AccessHistory
    performance_stats: CachePerformanceStats

    def __init__(self, **data):
        super().__init__(**data)
        self.replacement_policy.prepare(self.access_history, self.associativity)

    def process_request(self, address: int) -> None:
        set_index, tag = self._decode_address(address)
        found, slot = self.cache_table.find_tag_in_line(set_index, tag)

        if found:
            self.performance_stats.increment_hit()
        else:
            self._replace_cache_line(tag, set_index)

    def _decode_address(self, address: int) -> tuple[int, int]:
        index_bits = int(math.log2(self.num_sets))
        offset_bits = int(math.log2(self.block_size))
        set_index = (address >> offset_bits) & ((1 << index_bits) - 1)
        tag = address >> (offset_bits + index_bits)
        return set_index, tag

    def _replace_cache_line(self, tag: int, set_index: int):
        cache_line = self.cache_table.get_cache_line(set_index)
        replacement_index = self.replacement_policy.select_replacement_index(
            set_index, cache_line, self.access_history
        )
        new_entry = {"tag": tag}
        self.cache_table.update_cache_line(set_index, replacement_index, new_entry)
        if cache_line[replacement_index] is None:
            self.performance_stats.increment_error("Compulsory")
        else:
            self.performance_stats.increment_error("Conflict")


def get_cache_from_config(config: CacheConfig):
    replacement_policy = get_replacement_policy(config.pol)
    cache_table = CacheTable(config.n_sets, config.assoc)

    cache = Cache(
        num_sets=config.n_sets,
        block_size=config.b_size,
        associativity=config.assoc,
        replacement_policy=replacement_policy,
        access_history=AccessHistory(
            history=[[i for i in range(config.assoc)] for _ in range(config.n_sets)]
        ),
        performance_stats=CachePerformanceStats(),
        cache_table=cache_table,
    )
    return cache
