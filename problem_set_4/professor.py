import random

def main():

    level = get_level()
    
    score = 0
    for i in range(10):

        X = generate_integer(level)
        Y = generate_integer(level)
        ans = str(X + Y)
        
        correct = False
        tries = 0

        while ((not correct) and (tries < 3)):
            attempt = input(f"{X} + {Y} = ")
            if attempt == ans:
                correct = True
                score = score + 1
            else:
                print("EEE")
                tries = tries + 1

        if correct == False:
            print(f"{X} + {Y} = {ans}")

    print("Score:", score)


def get_level():

    get_number = False
    while not get_number:
        lv = input("Level: ")
        if lv in ['1', '2', '3']:
            get_number = True
    return int(lv)


def generate_integer(level):

    return random.randint(pow(10, level-1), pow(10, level)-1)
        



if __name__ == "__main__":
    main()