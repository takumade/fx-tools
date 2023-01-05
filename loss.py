import math
from lib.ProfitLoss import ProfitLoss


def calculateLoss():
    print("LOSS CALCULATOR\n")
    entryPrice = float(input("Entry price: "))
    stopLoss = float(input("Stop Loss: "))
    lotSize = float(input("Lot Size: "))
    positions = int(input("Positions: "))
    
    profitLoss = ProfitLoss(entryPrice, lotSize, positions)
    pips, loss =profitLoss.calculateLoss(stopLoss)
    
    print("Total Pips: ", pips)
    print("Loss: ", loss)
    
    
      
calculateLoss()