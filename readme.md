<h1 align="center">Byte Chomp</h1>
<h2 align="center">Cache Simulation</h2>

<p align="center">
  <img src="images/byte_chomp.png" width="30%" />
</p>


## Installation

```bash
pip install -r requirements.txt
```


## Running the Cache Simulator

The cache simulator uses command-line arguments for configuration. You can run the simulator using the following command:

```bash
python cache_simulator.py <n_sets> <b_size> <assoc> <pol> <output_flag> <filename>
```

### Input Arguments

- `n_sets`: Number of sets (integer).
- `b_size`: Block size in bytes (integer).
- `assoc`: Associativity degree (integer).
- `pol`: Replacement policy (string).
- `output_flag`: Flag that activates the standard output mode of data (integer).
- `filename`: Name of the input file containing the addresses (string).


## Running Tests


```bash
pytest
```

This command runs all the tests written with pytest, ensuring the simulator behaves as expected under various configurations.