import requests
import sys


try:
    if len(sys.argv) == 2:

        n=float( sys.argv[1])
                

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        file = response.json()
        r = file["bpi"]["USD"]["rate"]
        data = float(r.replace(",",""))
        result = data * n

        print(f"${result:,.4f}")
    else:
        sys.exit()    

except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument ")
    