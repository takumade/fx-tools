# FX Tools
Tools for trading Deriv's Synthentic Indices. Written in Python


## Tools

Check the `tools` folder

1. `profit.py` - Calculate profit given entry price, take profit, lot size and positions
2. `loss.py` - Calculate loss given entry price, stop loss, lot size and positions
3. `get_take_profit.py` - Calculate a take profit given

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
