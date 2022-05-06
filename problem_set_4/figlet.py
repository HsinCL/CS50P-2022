import sys
from pyfiglet import Figlet
from random import choice

if ((len(sys.argv) != 1) and (len(sys.argv) != 3)):
    print("Invalid usage")
else:
    if len(sys.argv) == 1:
        text = input("Input: ")
        f = Figlet()

        fontList = f.getFonts()
        rf = choice(fontList)
        f.setFont(font=rf)
        print(f.renderText(text))

    elif len(sys.argv) == 3:
        if ((sys.argv[1] != "-f") and (sys.argv[1] != "--font")):
            print("Invalid usage")
            sys.exit()
        try:
            f = Figlet(font=sys.argv[2])
        except:
            print("Invalid usage")
            sys.exit()
        else:
            text = input("Input: ")
            print(f.renderText(text))
        
    else:
        print("Invalid usage")
        sys.exit()


