import math


def calculateProfit():
    print("PROFIT CALCULATOR\n")
    
    entryPrice = float(input("Entry price: "))
    takeProfit = float(input("Take profit: "))
    lotSize = float(input("Lot Size: "))
    positions = int(input("Positions: "))
    
    totalPips = takeProfit - entryPrice
    yourProfit = (totalPips * lotSize) * positions
    
    print("Total Pips: ", totalPips)
    print("Your profit: ",abs(yourProfit))
    return abs(yourProfit)
    
      
calculateProfit()