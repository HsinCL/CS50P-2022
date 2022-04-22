def hello_func(to="world"):
    print(f"hello, {to}")


def main():
    # Ask user for user's name
    name = input("Whta's your name? ")

    # Say hello to user
    print("hello,", name)
    print("hello, "+ name)
    # print automatically insert a space between two arguments
    # print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

    # Remove whitespace from str and capitalize user's name
    name = name.strip().title() 

    # format string
    print(f"hello, {name}")

    hello_func(name)

    calculator()


def calculator():
    x = int(input("What's x? "))
    print("x squared is", square(x))

    # print(f"{x:,}")
    # print(f"{x:.2f}")


def square(n):
    return n ** 2 # pow(n, 2) 
    

main()