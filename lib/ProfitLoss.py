class ProfitLoss:
    
    def __init__(self, entryPrice, lotSize=0.2, positions=1):
        self.entryPrice = entryPrice
        self.lotSize = lotSize
        self.positions = positions 
    
    
    def calculateLoss(self, stopLoss):
        totalPips = stopLoss - self.entryPrice
        yourLoss = (totalPips * self.lotSize) * self.positions
        
        return [totalPips, -abs(yourLoss)]
    
    
    def calculateProfit(self):
        pass 
    
    
    