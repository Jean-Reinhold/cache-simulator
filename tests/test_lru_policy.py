from tests.fixtures import run_test_case


def test_lru_replacement_bin_100():
    expected_stats = {
        "requests": 100,
        "hit_rate": 0.46,
        "miss_rate": 0.54,
        "compulsory": 0.30,
        "capacity": 0.67,
        "conflict": 0.04,
    }
    run_test_case(2, 1, 8, "L", "bin_100.bin", expected_stats, 0.005)


def test_lru_replacement_vortex_persons():
    expected_stats = {
        "requests": 186676,
        "hit_rate": 0.5756,
        "miss_rate": 0.4244,
        "compulsory": 0.00,
        "capacity": 1.00,
        "conflict": 0.00,
    }
    run_test_case(1, 4, 32, "L", "vortex.in.sem.persons.bin", expected_stats, 0.001)
