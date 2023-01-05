import math
from lib.ProfitLoss import ProfitLoss

def calculateRiskReward():
    print("ROSK REWARD CALCULATOR\n")
    
    entryPrice = float(input("Entry price: "))
    takeProfit = float(input("Take profit: "))
    stopLoss = float(input("Stop loss: "))
    lotSize = float(input("Lot Size: "))
    positions = int(input("Positions: "))
    
    profitLoss = ProfitLoss(entryPrice, lotSize, positions)
    ppips, profit = profitLoss.calculateProfit(takeProfit)
    lpips, loss = profitLoss.calculateLoss(stopLoss)
    
    riskReward = profitLoss.calculateRiskReward(profit, loss)
    
    
    print("Profit: ", profit)
    print("Loss: ", loss)
    print("Risk Reward: {0}:{1}".format(riskReward[0], riskReward[1]))
    
      
calculateRiskReward()

