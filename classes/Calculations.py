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

    
    def calculate_stop_loss(self):
        
        positions = self.variables['positions']
        lot_size = self.variables['lot_size']
        entry_price = self.variables['entry_price']
        loss_amount = self.variables['loss_amount']
        
        
        stop_loss_buy  = ((loss_amount/ positions) / lot_size) - entry_price
        stop_loss_sell  = ((loss_amount/ positions) / lot_size) + entry_price

        return [abs(stop_loss_buy), abs(stop_loss_sell)]
    
    def caculate_stop_loss_take_profit():
        # Get Take Profit and Stop Loss given 
        # 1. Entry Point 
        # 2. Lose amount 
        # 3. Lot size
        # 4. Risk reward 

        # Algorithm
        # 1. Calculate SL using Lose Amount, Entry Point and Lot Size 
        # 2. Calculate the difference between SL and Entry Point
        # 3. Multiply the difference from 2 by the risk ratio
        # 4. Multiply the difference from 2 by reward ratio
        # 5. Add result from 4 to entry point to get TP
        # Print TP

        pass
    
    def calculate_lot_size(self):
        entry_price = self.variables['entry_price']
        stop_loss = self.variables['stop_loss']
        loss_amount = self.variables['loss_amount']
        
        lot_size = loss_amount / (entry_price-stop_loss) 
        
        return round(abs(lot_size), 2)
