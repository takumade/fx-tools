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
    
    
    # def calculateRiskReward(self, profit, loss):        
    #     return [abs(int(loss/loss)), abs(int(profit/loss))]

    
    # def calculateStopLoss(self, loss, buyOrSell):
        
    #     stopLoss = 0
        
    #     if buyOrSell  == 'b':
    #         stopLoss  = ((loss/self.positions) / self.lotSize) - self.entryPrice
    #     elif buyOrSell == 's':
    #         stopLoss  = ((loss/self.positions) / self.lotSize) + self.entryPrice
    #     else:
    #         stopLoss  = ((loss/self.positions) / self.lotSize) - self.entryPrice
    #     return abs(stopLoss)