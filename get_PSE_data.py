import pandas as pd
import json
import requests

# get the data using requests
data1 = requests.get('http://phisix-api3.appspot.com/stocks.json')

# deserialize JSON into Python object
data2 = json.loads(data1.text)

com_name = []
symbol = []
price = []
pct_chg = []
vol = []

for a in range(0, len(data2['stock'])-8):
    com_name.append(data2['stock'][a]['name'])
    symbol.append(data2['stock'][a]['symbol'])
    price.append(data2['stock'][a]['price']['amount'])
    pct_chg.append(data2['stock'][a]['percent_change'])
    vol.append(data2['stock'][a]['volume'])
    
df = pd.DataFrame([com_name, symbol, price, pct_chg, vol]).T
df.columns = ['Company Name', 'Symbol', 'Price', 'Pct. Chg.', 'Volume']

add_text = data2['as_of'][:10] # for title

df.to_csv(f'PSE_{add_text}.csv', index=None)
df.to_html(f'PSE_{add_text}.html', index=None)