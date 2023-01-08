class FXTools:
    
    def __init__(self):
        self.variables = {}
    
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
    
    # def calculateLoss(self, stopLoss):
    #     totalPips = stopLoss - self.entryPrice
    #     yourLoss = (totalPips * self.lotSize) * self.positions
        
    #     return [ round(abs(totalPips),1),   # pips
    #             round(-abs(yourLoss),2) ]   # loss
    
    
    # def calculateProfit(self, takeProfit):
    #     totalPips = takeProfit - self.entryPrice
    #     yourProfit = (totalPips * self.lotSize) * self.positions
        
    #     return [round(abs(totalPips),1), # pips
    #             round(abs(yourProfit),2)]  # loss
    
    
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