# FX Tools
Tools for trading Deriv's Synthentic Indices. Written in Python


## Tools

Check the `tools` folder
*NOTE:* Tools are interactive so just run `python tool_name.py`

1. `fx-tools.py` - Run CLI mode or Interactive mode
2. `profit.py` - Calculate profit given entry price, take profit, lot size and positions
3. `loss.py` - Calculate loss given entry price, stop loss, lot size and positions
4. `stop_loss.py` - Calculate a stop loss given entry price, loss amount, lot size and position
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

Setting variables

```sh
FX-Tools> set stop_loss 5265.25621
FX-Tools> set loss_amount 20
FX-Tools> set take_profit 56267.256
FX-Tools> set risk_reward 1:2
```

Get variables

```sh
FX-Tools> get stop_loss 
5265.25621
FX-Tools> get loss_amount 
20
FX-Tools> get take_profit 
56267.256
FX-Tools> get risk_reward 
1:2
```

Executing a tool

```sh
FX-Tools> exec get_stop_loss 
FX-Tools> exec risk_reward
```

Getting Help



## CLI Mode

Coming Soon!