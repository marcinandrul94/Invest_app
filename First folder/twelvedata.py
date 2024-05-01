
import pandas as pd
import requests
import json
'''https://twelvedata.com/docs#errors
https://api.twelvedata.com'''


def get_keys(path):
    with open(path) as f:
        return json.load(f)

keys = get_keys("First folder\.secret\secret.json")
API_Key = keys["API_KEY"]


r = requests.get(f"https://api.twelvedata.com/stocks?exchange=NYSE&mic_code=XNYS&type=Common Stock&apikey={API_Key}")




try:
    stocks = r.json()
except json.decoder.JSONDecodeError:
    print('Niepoprawny format')
else:
    print(stocks["data"][1000])

#Calculates the number of records in a request
print(len(stocks["data"]))