import pytest
from cache_simulator import process_file
from byte_chomp.models import CacheConfig

TEST_ADDRESS_DIR = "tests/addresses"


def run_test_case(
    n_sets: int,
    b_size: int,
    assoc,
    pol: str,
    filename: str,
    expected_stats: dict[str, float],
    tolerance: float = 0.005,
):
    config = CacheConfig(
        n_sets=n_sets,
        b_size=b_size,
        assoc=assoc,
        pol=pol,
        output_flag=0,
        filename=f"{TEST_ADDRESS_DIR}/{filename}",
    )
    report = process_file(config=config)
    print(report)
    print(expected_stats)
    assert report["requests"] == expected_stats["requests"]
    assert abs(report["hit_rate"] - expected_stats["hit_rate"]) <= tolerance
    assert abs(report["miss_rate"] - expected_stats["miss_rate"]) <= tolerance
    assert abs(report["compulsory"] - expected_stats["compulsory"]) <= tolerance
    assert abs(report["capacity"] - expected_stats["capacity"]) <= tolerance
    assert abs(report["conflict"] - expected_stats["conflict"]) <= tolerance
