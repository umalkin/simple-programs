import pandas as pd

from urllib.request import urlopen

aad = []

for a in ['0-9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
    aa = urlopen('https://en.wikipedia.org/wiki/Companies_listed_on_the_New_York_Stock_Exchange_(%s)' %  a ).read()
    aaf = pd.read_html(aa)
    data = aaf[1]
    aad.append(data)

aad = pd.concat(aad)

aad.to_csv('aa.csv', index=None)
    



