def coin_change_greedy(coins:list, amt:int):
    i = len(coins)-1
    count = 0
    while amt > 0:
        while i > 0 and coins[i] > amt:
            i -= 1
        amt -= coins[i]
        count += 1
    return count if amt==0 else -1

if __name__ == "__main__":
    coins = [1,5,10,20,50,100]
    amt = 131
    res = coin_change_greedy(coins=coins, amt=amt)
    print(res)