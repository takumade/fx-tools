import math


def calculateLoss():
    print("LOSS CALCULATOR\n")
    entryPrice = float(input("Entry price: "))
    stopLoss = float(input("Stop Loss: "))
    lotSize = float(input("Lot Size: "))
    positions = int(input("Positions: "))
    
    totalPips = stopLoss - entryPrice
    yourLoss = (totalPips * lotSize) * positions
    
    print("Total Pips: ", totalPips)
    print("Your loss: ", -abs(yourLoss))
    return abs(yourLoss)
    
    
      
calculateLoss()