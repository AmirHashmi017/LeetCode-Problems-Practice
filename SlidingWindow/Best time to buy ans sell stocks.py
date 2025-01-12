def maxProfit(prices):
    left=0
    right=1
    maxprofit=0
    while(right<len(prices)):
        profit=prices[right]-prices[left]
        if(profit>0):
            maxprofit=max(maxprofit,profit)
        else:
            left=right
        right+=1
    
    return maxprofit
        

prices=[2,1,2,0,1]
print(maxProfit(prices))