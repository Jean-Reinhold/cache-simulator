import pytest
from cache_simulator import process_file
from byte_chomp.models import CacheConfig

TOLERANCE = 0.005

TEST_ADDRESS_DIR = "tests/addresses"


def test_cache_simulation_bin_100():
    config = CacheConfig(
        n_sets=256,
        b_size=4,
        assoc=1,
        pol="R",
        output_flag=1,
        filename=f"{TEST_ADDRESS_DIR}/bin_100.bin",
    )
    expected_stats = {
        "requests": 100,
        "hit_rate": 0.92,
        "miss_rate": 0.08,
        "compulsory": 1.00,
        "capacity": 0.00,
        "conflict": 0.00,
    }

    report = process_file(config=config)
    assert report["requests"] == expected_stats["requests"]
    assert abs(report["hit_rate"] - expected_stats["hit_rate"]) <= TOLERANCE
    assert abs(report["miss_rate"] - expected_stats["miss_rate"]) <= TOLERANCE
    # assert abs(report.get("compulsory", 0) - expected_stats.get("compulsory", 0)) <= TOLERANCE
    # assert abs(report.get("capacity", 0) - expected_stats.get("capacity", 0)) <= TOLERANCE
    # assert abs(report.get("conflict", 0) - expected_stats.get("conflict", 0)) <= TOLERANCE


def test_cache_simulation_bin_1000():
    config = CacheConfig(
        n_sets=128,
        b_size=2,
        assoc=4,
        pol="R",
        output_flag=1,
        filename=f"{TEST_ADDRESS_DIR}/bin_1000.bin",
    )
    expected_stats = {
        "requests": 1000,
        "hit_rate": 0.864,
        "miss_rate": 0.136,
        "compulsory": 1.00,
        "capacity": 0.00,
        "conflict": 0.00,
    }

    report = process_file(config=config)
    assert report["requests"] == expected_stats["requests"]
    assert abs(report["hit_rate"] - expected_stats["hit_rate"]) <= TOLERANCE
    assert abs(report["miss_rate"] - expected_stats["miss_rate"]) <= TOLERANCE
    # assert abs(report.get("compulsory", 0) - expected_stats.get("compulsory", 0)) <= TOLERANCE
    # assert abs(report.get("capacity", 0) - expected_stats.get("capacity", 0)) <= TOLERANCE
    # assert abs(report.get("conflict", 0) - expected_stats.get("conflict", 0)) <= TOLERANCE


def test_cache_simulation_bin_10000():
    config = CacheConfig(
        n_sets=16,
        b_size=2,
        assoc=8,
        pol="R",
        output_flag=1,
        filename=f"{TEST_ADDRESS_DIR}/bin_10000.bin",
    )
    expected_stats = {
        "requests": 10000,
        "hit_rate": 0.9298,
        "miss_rate": 0.0702,
        "compulsory": 0.18,
        "capacity": 0.79,
        "conflict": 0.03,
    }

    report = process_file(config=config)
    assert report["requests"] == expected_stats["requests"]
    assert abs(report["hit_rate"] - expected_stats["hit_rate"]) <= TOLERANCE
    assert abs(report["miss_rate"] - expected_stats["miss_rate"]) <= TOLERANCE
    # assert abs(report.get("compulsory", 0) - expected_stats.get("compulsory", 0)) <= TOLERANCE
    # assert abs(report.get("capacity", 0) - expected_stats.get("capacity", 0)) <= TOLERANCE
    # assert abs(report.get("conflict", 0) - expected_stats.get("conflict", 0)) <= TOLERANCE


def test_cache_simulation_vortex_persons_config1():
    config = CacheConfig(
        n_sets=512,
        b_size=8,
        assoc=2,
        pol="R",
        output_flag=1,
        filename=f"{TEST_ADDRESS_DIR}/vortex.in.sem.persons.bin",
    )
    expected_stats = {
        "requests": 186676,
        "hit_rate": 0.8782,
        "miss_rate": 0.1218,
        "compulsory": 0.05,
        "capacity": 0.93,
        "conflict": 0.02,
    }

    report = process_file(config=config)
    assert report["requests"] == expected_stats["requests"]
    assert abs(report["hit_rate"] - expected_stats["hit_rate"]) <= TOLERANCE
    assert abs(report["miss_rate"] - expected_stats["miss_rate"]) <= TOLERANCE
    # assert abs(report.get("compulsory", 0) - expected_stats.get("compulsory", 0)) <= TOLERANCE
    # assert abs(report.get("capacity", 0) - expected_stats.get("capacity", 0)) <= TOLERANCE
    # assert abs(report.get("conflict", 0) - expected_stats.get("conflict", 0)) <= TOLERANCE


def test_cache_simulation_vortex_persons_config2():
    config = CacheConfig(
        n_sets=1,
        b_size=4,
        assoc=32,
        pol="R",
        output_flag=1,
        filename=f"{TEST_ADDRESS_DIR}/vortex.in.sem.persons.bin",
    )
    expected_stats = {
        "requests": 186676,
        "hit_rate": 0.544,
        "miss_rate": 0.456,
        "compulsory": 0.00,
        "capacity": 1.00,
        "conflict": 0.00,
    }

    report = process_file(config=config)
    assert report["requests"] == expected_stats["requests"]
    assert abs(report["hit_rate"] - expected_stats["hit_rate"]) <= TOLERANCE
    assert abs(report["miss_rate"] - expected_stats["miss_rate"]) <= TOLERANCE
    # assert abs(report.get("compulsory", 0) - expected_stats.get("compulsory", 0)) <= TOLERANCE
    # assert abs(report.get("capacity", 0) - expected_stats.get("capacity", 0)) <= TOLERANCE
    # assert abs(report.get("conflict", 0) - expected_stats.get("conflict", 0)) <= TOLERANCE
