from tests.fixtures import run_test_case


def test_fifo_replacement_bin_100():
    expected_stats = {
        "requests": 100,
        "hit_rate": 0.43,
        "miss_rate": 0.57,
        "compulsory": 0.28,
        "capacity": 0.68,
        "conflict": 0.04,
    }
    run_test_case(2, 1, 8, "F", "bin_100.bin", expected_stats, 0.005)


def test_fifo_replacement_vortex_persons():
    expected_stats = {
        "requests": 186676,
        "hit_rate": 0.553,
        "miss_rate": 0.447,
        "compulsory": 0.00,
        "capacity": 1.00,
        "conflict": 0.00,
    }
    run_test_case(1, 4, 32, "F", "vortex.in.sem.persons.bin", expected_stats, 0.001)
