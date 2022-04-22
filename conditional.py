def is_even(n):
    return (n % 2 == 0)

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

    #if 90 <= x <= 100:
    #    print("A")
    #else:
    #    print("below A")

main()