import math
from classes.FXTools import ProfitLoss

def calculateProfit():
    print("PROFIT CALCULATOR\n")
    
    entryPrice = float(input("Entry price: "))
    takeProfit = float(input("Take profit: "))
    lotSize = float(input("Lot Size: "))
    positions = int(input("Positions: "))
    
    profitLoss = ProfitLoss(entryPrice, lotSize, positions)
    pips, profit = profitLoss.calculateProfit(takeProfit)
    
    print("Total Pips: ", pips)
    print("Profit: ", profit)
    
      
calculateProfit()