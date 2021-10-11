import pandas as pd
# from datetime import
from plotly.offline import plot
from plotly.graph_objs import Figure, Scatter, Bar
import plotly.graph_objs.layout as go

# Pagkuha ng data
data = pd.read_excel('ele.xlsx')

# Magdagdag ng isa kada buwan.
haba = 117

# Kunin lamang ang mga kakailanganing data.
data = data[:haba]

# Gawing buwan at taon lang ang nasa column na Month Year.
#data['Month Year'] = [month.strftime('%y-%m') for month in data['Month Year'][:haba]]

# Pagpa-Plot
fig = Figure()

fig.add_trace(Scatter(x=data['Month Year'], y=data['Total Current Amount'], name='Binayaran'))
fig.add_trace(Scatter(x=data['Month Year'], y=data['Subsidies/Refunds'], name='Diskuwento'))
fig.add_trace(Bar(x=data['Month Year'], y=data['Total w/out Subsidies'], name='Kabuuan'))

fig.layout.xaxis = go.XAxis(title=go.xaxis.Title(text='Buwan/Taon'))
fig.layout.yaxis = go.YAxis(title=go.yaxis.Title(text='Halaga (P)'))

fig.layout.title = 'Aming Bayarin sa Kuryente sa Loob ng Siyam na Taon'

# I-save ang ginawang plot bilang HTML.
plot(fig, filename='kuryente.html')
