# FX Tools
Tools for trading Deriv's Synthentic Indices. Written in Python


## Tools

Check the `tools` folder
*NOTE:* Tools are interactive so just run `python tool_name.py e.g python profit.py`

1. `fx-tools.py -i` - Run in Interactive mode
2. `stop_loss.py` - Calculate a stop loss given entry price, loss amount, lot size and position
5. `risk_reward.py` - Calculate risk reward given entry price, SL, TP , lot size and positions 
6. `profit_loss_take_profit` - Calculate risk reward given entry price, loss amount, 

## Installation
1. Install `virtualenv`
    ```python
    pip3 install virtualenv
    ```
2. Create a virtual environment
    ```python
    cd fx-tools && python3 -m virtualenv env
    ```
3. Install modules
    ```sh
    source env/bin/activate
    pip3 install -r requirements.txt
    ```
4. Have fun
    ```sh
    python3 profit-calculator.py  # Run profit calculator tool
    ```

*Note:* You run step 1 to 3 once

## Update

1. Pull changes 
    ```sh 
    git pull origin main
    ```
3. Install modules
    ```sh
    pip3 install -r requirements.txt
    ```
4. Have fun


## Interactive Mode

Coming Soon!

To enter interactive mode type 

```sh
python fx-tools.py -i 
```

### Setting variables

```sh
fx-tools> set stop_loss 5265.25621
fx-tools> set loss_amount 20
fx-tools> set take_profit 56267.256
fx-tools> set risk_reward 1:2
```

### Get variables

```sh
fx-tools> get stop_loss 
5265.25621
fx-tools> get loss_amount 
20
fx-tools> get take_profit 
56267.256
fx-tools> get risk_reward 
1:2
```

### Executing a tool

```sh
fx-tools> run get_stop_loss 
fx-tools> run risk_reward
```

Getting Help

```sh
fx-tools> help
fx-tools> help tool <tool_name>
```
