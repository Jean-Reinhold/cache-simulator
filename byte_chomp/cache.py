import math
from pydantic import BaseModel

from byte_chomp.models import (
    CachePerformanceStats,
    CacheTable,
    CacheConfig,
)
from byte_chomp.replacement_policies import ReplacementStrategy, get_replacement_policy


class Cache(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    num_sets: int
    block_size: int
    associativity: int
    replacement_policy: ReplacementStrategy
    cache_table: CacheTable
    performance_stats: CachePerformanceStats

    @property
    def index_bits(self) -> int:
        return int(math.log2(self.num_sets))

    @property
    def offset_bits(self) -> int:
        return int(math.log2(self.block_size))

    def process_request(self, address: int) -> None:
        index, tag = self._decode_address(address)
        found, slot = self.cache_table.find_tag_in_line(index, tag)

        if found:
            self.performance_stats.hits += 1
            self.replacement_policy.update_access(index, slot)
        else:
            self._replace_cache_line(tag, index)
            self.replacement_policy.update_access(index, slot)

    def _decode_address(self, address: int) -> tuple[int, int]:
        index = (address >> self.offset_bits) & ((1 << self.index_bits) - 1)
        tag = address >> (self.offset_bits + self.index_bits)
        return index, tag

    def _replace_cache_line(self, tag: int, index: int):
        cache_line = self.cache_table.get_cache_line(index)
        replacement_slot = self.replacement_policy.select_replacement_slot(
            index, cache_line
        )

        if cache_line[replacement_slot] is None:
            self.performance_stats.compulsory += 1
        elif self.cache_table.is_full():
            self.performance_stats.capacity += 1
        else:
            self.performance_stats.conflict += 1

        new_entry = {"tag": tag}
        self.cache_table.update_cache_line(index, replacement_slot, new_entry)


def get_cache_from_config(config: CacheConfig):
    replacement_policy = get_replacement_policy(config.pol)
    cache = Cache(
        num_sets=config.n_sets,
        block_size=config.b_size,
        associativity=config.assoc,
        replacement_policy=replacement_policy,
        performance_stats=CachePerformanceStats(compact_output=config.output_flag),
        cache_table=CacheTable(num_sets=config.n_sets, associativity=config.assoc),
    )
    return cache
