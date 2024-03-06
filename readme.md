
# Byte Chomp

Byte Chomp is a cache simulator developed in Python, created as part of the Computer Architecture and Organization 2 course by students Jean Reinhold and Luísa Ribeiro. The project's goal is to facilitate the understanding and analysis of cache behavior under different configurations and replacement policies.

Byte Chomp é um simulador de caches desenvolvido em Python, criado como parte da disciplina de Arquitetura e Organização de Computadores 2 pelos alunos Jean Reinhold e Luísa Ribeiro. O objetivo do projeto é facilitar o entendimento e a análise do comportamento de caches sob diferentes configurações e políticas de substituição.

- [Installation/Instalação](#installationinstalação)
- [Usage/Uso](#usageuso)
- [Running Tests/Executando Testes](#running-testsexecutando-testes)
- [Project Structure/Estrutura do Projeto](#project-structureestrutura-do-projeto)
- [GitHub Codespaces](#github-codespaces)
- [Contributions/Contribuições](#contributionscontribuições)

![Byte Chomp](images/byte_chomp.png)

## Installation/Instalação

To install the necessary dependencies for Byte Chomp, run the following command:

Para instalar as dependências necessárias do Byte Chomp, execute o seguinte comando:

```bash
pip install -r requirements.txt
```

Python `3.9` is also required, but later versions should work as well.

Também é necessário Python `3.9`, mas versões superiores devem funcionar.

## Usage/Uso

The Byte Chomp cache simulator is configured and executed through command line arguments. Use the following command to run the simulator:

O simulador de cache Byte Chomp é configurado e executado por meio de argumentos na linha de comando. Use o seguinte comando para rodar o simulador:

```bash
python cache_simulator.py <n_sets> <b_size> <assoc> <pol> <output_flag> <filename>
```

### Input Arguments/Argumentos de Entrada

- `n_sets`: Number of sets (integer). / Número de conjuntos (inteiro).
- `b_size`: Block size in bytes (integer). / Tamanho do bloco em bytes (inteiro).
- `assoc`: Degree of associativity (integer). / Grau de associatividade (inteiro).
- `pol`: Replacement policy (string). / Política de substituição (string).
- `output_flag`: Flag to activate standard output mode of data (integer). / Flag que ativa o modo de saída padrão dos dados (inteiro).
- `filename`: Name of the input file containing addresses (string). / Nome do arquivo de entrada contendo os endereços (string).

## Running Tests/Executando Testes

To ensure the simulator is working as expected under various configurations, run the tests written with pytest using the following command:

Para garantir que o simulador esteja funcionando conforme esperado sob várias configurações, execute os testes escritos com pytest usando o seguinte comando:

```bash
pytest
```

## GitHub Codespaces

The project is also set up to use GitHub Codespaces, allowing you to run tests in a pre-configured environment in a simplified manner. To open a Codespace:

Além disso, o projeto está configurado para usar o GitHub Codespaces, permitindo que você execute os testes de maneira simplificada em um ambiente já configurado. Para abrir um Codespace:

1. Go to the GitHub repository of the Byte Chomp project. / Vá ao repositório do GitHub do projeto Byte Chomp.
2. Click on "Code" and, in the dropdown menu, select "Open with Codespaces". / Clique em "Code" e, no menu suspenso, selecione "Open with Codespaces".
3. Click on "New codespace" to create a new environment. / Clique em "New codespace" para criar um novo ambiente.

## Project Structure/Estrutura do Projeto

The directory structure of the Byte Chomp project is as follows:

A estrutura de diretórios do projeto Byte Chomp é a seguinte:

```
.
├── Dockerfile
├── LICENSE
├── byte_chomp
│   ├── __init__.py
│   ├── argparser.py
│   ├── cache.py
│   ├── models.py
│   └── replacement_policies.py
├── cache_simulator.py
├── images
│   └── byte_chomp.png
├── pytest.ini
├── readme.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── addresses
    │   ├── bin_100.bin
    │   ├── bin_100.txt
    │   ├── bin_1000.bin
    │   ├── bin_1000.txt
    │   ├── bin_10000.bin
    │   ├── bin_10000.txt
    │   ├── vortex.in.sem.persons.bin
    │   └── vortex.in.sem.persons.txt
    ├── fixtures.py
    ├── test_fifo_policy.py
    ├── test_lru_policy.py
    └── test_random_policy.py
```

## Contributions/Contribuições

To contribute to the Byte Chomp project, please send a pull request or open an issue in the project's GitHub repository detailing your suggestion or contribution.

Para contribuir com o projeto Byte Chomp, por favor, envie um pull request ou abra uma issue no repositório do projeto detalhando a sua sugestão ou contribuição.