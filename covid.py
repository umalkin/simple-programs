import pandas as pd
import json

name = input('Pangalan ng file : ')

file = json.load(open(f'{name}.json'))

data = pd.DataFrame(file['data'])
data.drop(['region_res', 'prov_res', 'city_mun_res', 'city_muni_psgc'], axis=1, inplace=True)

data.sort_values(['date_specimen'], inplace=True)

data.to_csv(f'{name}.csv', index=None)
