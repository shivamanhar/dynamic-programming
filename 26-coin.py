money, m = map(int,raw_input().split())
coins = list(map(int,raw_input().split()))
processed={}

def change(coins,money,idx,processed):
    if not money:
        return 1
    if idx >= len(coins):
        return 0
    amt=0
    changes=0
    key =str(money) + '-' + str(idx)
    if key in processed.keys():
        return processed[key]
    
    while(amt <= money):
        rem = money-amt
        changes += change(coins,rem,idx+1,processed)
        amt += coins[idx]
    processed[key] = changes
    return changes
        
print(change(coins,money,0,processed))