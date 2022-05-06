from random import choice

secret_number = 0
while True:
    
    try:
        level = int(input("Level: "))
    except:
        pass
    else:
        if (level > 0):
            secret_number = choice(range(1, level+1))
            break
        else:
            continue 

guess_right = False
while not guess_right:

    try:
        guess = int(input("Guess: "))
    except:
        pass
    else:
        if (level > 0):
            if guess > secret_number:
                print("Too large!")
            elif guess < secret_number:
                print("Too small!")
            else:
                print("Just right!")
                break
        else:
            continue

