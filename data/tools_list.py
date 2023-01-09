tools_list = {
    'loss': {
        'name': 'loss',
        'desc': 'Calculate loss given entry point, stop loss, lot size and positions',
        'requires': [
            'entry_price',
            'lot_size',
            'positions',
            'stop_loss'  
        ] 
    },
    'profit': {
        'name': 'profit',
        'desc': 'Calculate profit given entry point, take profit, lot size and positions',
        'requires': [
            'entry_price',
            'lot_size',
            'positions',
            'take_profit'  
        ] 
    }
}
