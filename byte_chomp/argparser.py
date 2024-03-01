from argparse import ArgumentParser

from byte_chomp.models import CacheConfig


def get_cache_config_parser() -> CacheConfig:
    parser = ArgumentParser(description="Enumere os valores de configuração da cache")

    parser.add_argument("n_sets", type=int, help="Número de conjuntos.")
    parser.add_argument("b_size", type=int, help="Tamanho do bloco em bytes.")
    parser.add_argument("assoc", type=int, help="Grau de associatividade.")
    parser.add_argument("pol", type=str, help="Política de substituição.")
    parser.add_argument(
        "output_flag", type=int, help="Flag que ativa o modo padrão de saída de dados"
    )
    parser.add_argument("filename", type=str, help="Nome do arquivo de entrada")

    return parser


def parse_cache_config(parser: ArgumentParser) -> CacheConfig:
    return CacheConfig(**vars(parser.parse_args()))
