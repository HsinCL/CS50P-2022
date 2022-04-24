amount_due = 50
while amount_due > 0:
    coin = int(input("coin: ")) # 25, 10, 5
    amount_due = amount_due - coin
    if amount_due > 0:
        print(f"Amount due = {amount_due}")
    else:
        print(f"Change owed = {-amount_due}") 