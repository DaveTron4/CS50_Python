import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

r = r.json()
rate = float(r["bpi"]["USD"]["rate_float"])
amount = rate * float(sys.argv[1])
print(f"${amount:,.4f}")
