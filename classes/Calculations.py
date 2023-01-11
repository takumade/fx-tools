class Calculations:
    
    def __init__(self):
        self.variables = {
            'positions': 1,
            'lot_size': 0.2,
            'entry_price': None,
            'stop_loss': None,
            'take_profit': None,
            'loss_amount': None
        }
    
    def set_variable(self, key, value):
        if key and value:
            self.variables[key] = value 
        else:
            raise ValueError
    
    def get_variable(self, key):
        if key: 
            return self.variables[key]
        else:
            raise ValueError
        
    def get_all_vars(self):
        print("\nAll Variables:\n")
        for k in self.variables:
            print("{0:25s}        : {1}".format(k, self.variables[k]))
    
    def calculate_loss(self):
        totalPips = float(self.variables['stop_loss']) - float(self.variables['entry_price'])
        yourLoss = (totalPips * float(self.variables['lot_size'])) * int(self.variables['positions'])
        
        return [ round(abs(totalPips),1),   # pips
                round(-abs(yourLoss),2) ]   # loss
    
    
    def calculate_profit(self):
        totalPips = float(self.variables['take_profit']) - float(self.variables['entry_price'])
        yourProfit = (totalPips * float(self.variables['lot_size'])) * int(self.variables['positions'])
        
        return [round(abs(totalPips),1), # pips
                round(abs(yourProfit),2)]  # profit
    
    
    def calculate_risk_reward(self):    
        ppips, profit = self.calculate_profit()
        lpips, loss = self.calculate_loss()
          
        return [abs(int(loss/loss)), abs(int(profit/loss)), profit, loss]

    
    def calculate_stop_loss(self, loss):
        
        positions = self.variables['positions']
        lot_size = self.variables['lot_size']
        entry_price = self.variables['entry_price']
        
        
        stop_loss_buy  = ((loss/ positions) / lot_size) - entry_price
        stop_loss_sell  = ((loss/ positions) / lot_size) + entry_price

        return [abs(stop_loss_buy), abs(stop_loss_sell)]