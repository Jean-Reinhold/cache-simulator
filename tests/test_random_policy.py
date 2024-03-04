from tests.fixtures import run_test_case


def test_random_replacement_bin_100():
    expected_stats = {
        "requests": 100,
        "hit_rate": 0.92,
        "miss_rate": 0.08,
        "compulsory": 1.00,
        "capacity": 0.00,
        "conflict": 0.00,
    }
    run_test_case(256, 4, 1, "R", "bin_100.bin", expected_stats)


def test_random_replacement_bin_1000():
    expected_stats = {
        "requests": 1000,
        "hit_rate": 0.864,
        "miss_rate": 0.136,
        "compulsory": 1.00,
        "capacity": 0.00,
        "conflict": 0.00,
    }
    run_test_case(128, 2, 4, "R", "bin_1000.bin", expected_stats)


def test_random_replacement_bin_10000():
    expected_stats = {
        "requests": 10000,
        "hit_rate": 0.9298,
        "miss_rate": 0.0702,
        "compulsory": 0.18,
        "capacity": 0.79,
        "conflict": 0.03,
    }
    run_test_case(16, 2, 8, "R", "bin_10000.bin", expected_stats, 0.01)


def test_random_replacement_vortex_persons_config1():
    expected_stats = {
        "requests": 186676,
        "hit_rate": 0.8782,
        "miss_rate": 0.1218,
        "compulsory": 0.05,
        "capacity": 0.93,
        "conflict": 0.02,
    }
    run_test_case(512, 8, 2, "R", "vortex.in.sem.persons.bin", expected_stats)


def test_random_replacement_vortex_persons_config2():
    expected_stats = {
        "requests": 186676,
        "hit_rate": 0.544,
        "miss_rate": 0.456,
        "compulsory": 0.00,
        "capacity": 1.00,
        "conflict": 0.00,
    }
    run_test_case(1, 4, 32, "R", "vortex.in.sem.persons.bin", expected_stats)
