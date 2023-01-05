class ProfitLoss:
    
    def __init__(self, entryPrice, lotSize=0.2, positions=1):
        self.entryPrice = entryPrice
        self.lotSize = lotSize
        self.positions = positions 
    
    
    def calculateLoss(self, stopLoss):
        totalPips = stopLoss - self.entryPrice
        yourLoss = (totalPips * self.lotSize) * self.positions
        
        return {"total_pips": round(abs(totalPips),1), 
                "total_loss": round(-abs(yourLoss),2)}
    
    
    def calculateProfit(self, takeProfit):
        totalPips = takeProfit - self.entryPrice
        yourLoss = (totalPips * self.lotSize) * self.positions
        
        return {"total_pips": round(abs(totalPips),1), 
                "total_profit": round(abs(yourLoss),2)}
    
    
    