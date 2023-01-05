import math
from lib.ProfitLoss import ProfitLoss

def calculateProfit():
    print("PROFIT CALCULATOR\n")
    
    entryPrice = float(input("Entry price: "))
    takeProfit = float(input("Take profit: "))
    lotSize = float(input("Lot Size: "))
    positions = int(input("Positions: "))
    
    profitLoss = ProfitLoss(entryPrice, lotSize, positions)
    result = profitLoss.calculateProfit(takeProfit)
    
    print("Total Pips: ", result["total_pips"])
    print("Your Profit: ", result["total_profit"])
    
      
calculateProfit()