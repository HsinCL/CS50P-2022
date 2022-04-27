def main():
    percentage = 100*get_fraction()
    if percentage < 1:
        print('E')
    elif percentage > 99:
        print('F')
    else: 
        print(f'{percentage:.0f}%')


def get_fraction():

    while True:
        prompt = input("Fraction: ")
        numbers = prompt.split('/')
        try:
            x = int(numbers[0])
            y = int(numbers[1])
        except ValueError: 
            pass
        else:
            try:
                return x/y
            except ZeroDivisionError:
                pass

        

main()
            
