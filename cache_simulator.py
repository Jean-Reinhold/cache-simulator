from byte_chomp.cache import get_cache_from_config
from byte_chomp.argparser import get_cache_config_parser, parse_cache_config


def main() -> None:
    parser = get_cache_config_parser()
    config = parse_cache_config(parser=parser)

    cache = get_cache_from_config(config=config)

    address = 0x1234
    cache.process_request(address)

    print(cache.performance_stats)


if __name__ == "__main__":
    main()
