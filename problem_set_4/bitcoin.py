import requests
import sys
import json

if len(sys.argv) == 1:
    print("Missing command-line argument")
else:
    try:
        n = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit()
    else:
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            table = response.json()
        except requests.RequestException:
            pass
        else:
            USD = n*table["bpi"]["USD"]["rate_float"]
            print(f"${USD:,.4f}")


