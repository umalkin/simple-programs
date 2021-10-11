import pandas as pd
from urllib.request import urlopen
# from bs4 import BeautifulSoup as bs

aad = []

for a in ['043400000', '042100000','041000000', '045600000', '045800000']:
    aa = urlopen('https://psa.gov.ph/classification/psgc/?q=psgc/citimuni/%s' %  a ).read()
    aaf = pd.read_html(aa)
    data = aaf[1]
    data1 = aaf[2]
    aad.append(data)
    aad.append(data1)

aad = pd.concat(aad)

aad.to_csv('aaaa.csv', index=None)
