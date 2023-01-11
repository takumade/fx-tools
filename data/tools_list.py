tools_list = {
    'risk': {
        'name': 'risk',
        'desc': 'Calculate loss/risk given entry price, stop loss, lot size and positions',
        'requires': [
            'entry_price',
            'lot_size',
            'positions',
            'stop_loss'  
        ] 
    },
    'reward': {
        'name': 'reward',
        'desc': 'Calculate profit/reward given entry price, take profit, lot size and positions',
        'requires': [
            'entry_price',
            'lot_size',
            'positions',
            'take_profit'  
        ] 
    },
    'risk_reward': {
        'name': 'risk_reward',
        'desc': 'Calculate risk reward ratio given entry price, take profit, stop loss, lot size and positions',
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
        'desc': 'Calculate stop loss given entry price, loss_amount, lot size and positions',
        'requires': [
            'entry_price',
            'lot_size',
            'positions',
            'loss_amount'
        ] 
    },
    'lot_size': {
        'name': 'lot_size',
        'desc': 'Calculate lot size given loss amount, entry price and  stop loss',
        'requires': [
            'entry_price',
            'stop_loss',
            'loss_amount'
        ] 
    }
    
}
