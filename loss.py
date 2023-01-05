import math
from lib.ProfitLoss import ProfitLoss


def calculateLoss():
    print("LOSS CALCULATOR\n")
    entryPrice = float(input("Entry price: "))
    stopLoss = float(input("Stop Loss: "))
    lotSize = float(input("Lot Size: "))
    positions = int(input("Positions: "))
    
    profitLoss = ProfitLoss(entryPrice, lotSize, positions)
    result = profitLoss.calculateLoss(stopLoss)
    
    print("Total Pips: ", result["total_pips"])
    print("Your loss: ", result["total_loss"])
    
    
      
calculateLoss()