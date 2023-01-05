import math
from lib.ProfitLoss import ProfitLoss

def calculateStopLoss():
    print("STOP LOSS CALCULATOR\n")
    
    entryPrice = float(input("Entry price: "))
    possibleLoss = float(input("Loss: "))

    lotSize = float(input("Lot Size: "))
    positions = int(input("Positions: "))
    
    profitLoss = ProfitLoss(entryPrice, lotSize, positions)
    buyStopLoss = profitLoss.calculateStopLoss(possibleLoss, 'b')
    sellStopLoss = profitLoss.calculateStopLoss(possibleLoss, 's')
    
    print("BUY stop loss: ", buyStopLoss)
    print("SELL stop loss: ", sellStopLoss)
    
      
calculateStopLoss()