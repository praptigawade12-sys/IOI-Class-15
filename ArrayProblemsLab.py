print("\n\nPART 1 - STOCK BUY-SELL AND PROFIT")
prices = [5,3,4,6,7,3,5]
profit = 0
for i in range(1,len(prices)):
    if prices[i] > prices[i-1]:
        profit += prices[i]-prices[i-1]
print("Prices :",prices)
print("Profit :",profit)

print("\n\nPART 2 - TALLEST BARS")
heigth = [0,1,0,2,1,0,1,3,2,1,2,1]
n = len(heigth)
left_tallest = [0]*n
left_tallest[0] = heigth[0]
for i in range(1,n):
    left_tallest[i] = max(left_tallest[i-1],heigth[i])
print("Heigth :",heigth)
print("Left Tallest :",left_tallest)

rigth_tallest = [0]*n
rigth_tallest[n-1] = heigth[n-1]
for i in range(n-2,-1,-1):
    rigth_tallest[i] = max(rigth_tallest[i+1],heigth[i])
print("Right Tallest :",rigth_tallest)

print("\n\nPART 3 - WATER TRAPPING")
water = 0
for i in range(n):
    water += min(left_tallest[i],rigth_tallest[i]) - heigth[i]
print("Total water trapped :",water)