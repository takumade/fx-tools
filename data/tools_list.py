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
    },
    'risk_reward': {
        'name': 'risk_reward',
        'desc': 'Calculate risk reward ratio given entry point, take profit, stop loss, lot size and positions',
        'requires': [
            'entry_price',
            'lot_size',
            'positions',
            'take_profit',
            'stop_loss'
        ] 
    },
    'stop_loss': {
        'name': 'stop_loss',
        'desc': 'Calculate stop loss given entry point, loss_amount, lot size and positions',
        'requires': [
            'entry_price',
            'lot_size',
            'positions',
            'loss_amount'
        ] 
    }
    
}
