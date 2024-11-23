candles=[4,4,1,3]
maxi=candles[0]
for i in range(1,len(candles)):
    if candles[i]>maxi:
        maxi=candles[i]
val=0
for i in range(len(candles)):
    if candles[i]==maxi:
        val+=1

print(val)


