import struct
import math

from byte_chomp.cache import get_cache_from_config
from byte_chomp.argparser import get_cache_config_parser, parse_cache_config


def read_binary_file(filename: str) -> bytes:
    with open(filename, "rb") as file:
        return file.read()


def convert_to_address(bin_file: bytes, word_size: int) -> list[tuple[int, int]]:
    addresses = []
    n_requests = len(bin_file) // word_size

    for i in range(n_requests):
        bin_word = bin_file[i * word_size : (i + 1) * word_size]
        addr = struct.unpack(">I", bin_word)[
            0
        ]  # Convert from big-endian binary to integer
        addresses.append(addr)

    return addresses


def process_file(config) -> None:
    cache = get_cache_from_config(config=config)

    bin_file_data = read_binary_file(config.filename)

    addresses = convert_to_address(bin_file_data, 4)

    for address in addresses:
        cache.process_request(address=address)

    return cache.performance_stats.report


if __name__ == "__main__":
    parser = get_cache_config_parser()
    config = parse_cache_config(parser=parser)

    report = process_file(config=config)

    print(report)
