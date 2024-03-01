from byte_chomp.argparser import get_cache_config_parser, parse_cache_config


def main() -> None:
    parser = get_cache_config_parser()
    config = parse_cache_config(parser=parser)

    print(config)


if __name__ == "__main__":
    main()
