def main():

    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total = 0
    while True:
        try:
            item = input("Item: ")
        except EOFError:  
            break
        else:
            total = cal_total(total, item, menu)
            #print(f"Total: ${total:.2f}")
    
    print('\n', end="")
    total = cal_total(total, item, menu)
    #print(f"\nTotal: ${total:.2f}")
    print("Item: ")
            


def cal_total(total, item, menu):
    item = item.title()
    if item in menu:
        total = total + menu[item]
        print(f"Total: ${total:.2f}")
    return total
    
    

    

main()