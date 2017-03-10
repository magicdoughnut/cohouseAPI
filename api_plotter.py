import pandas as pd
import datetime
import numpy as np


# Read our backups back in..
df_companies = pd.read_pickle('companies.pkl')
df_fillings = pd.read_pickle('fillings.pkl')

# np_thing = df_fillings['title'].as_matrix()

# print df_fillings.head()

# np_thing = df_fillings['date'].as_matrix()
# print np_thing

df_officer_change = df_fillings.query("category == 'officers'")
df_joined =  pd.merge(df_officer_change, df_companies, on='company_number', how='left')[['title', 'action_date']]

# print df_joined.head
np_date_list = df_joined['action_date'].as_matrix()
print len(np_date_list)

# date_store = []
# for date in np_date_list:
# 	if str(date) != 'nan':
# 		date_store.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
# 		# np.append(date_store,datetime.datetime.strptime(date, '%Y-%m-%d'))
# 	else:
# 		date_store.append('nan')
# 		# np.append(date_store,'nan')

# print(len(date_store))


df_joined['action_date'] = pd.to_datetime(df_joined['action_date'])
df_joined['zero'] = 0.0
print df_joined['action_date']

# exit()

import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('mdawson', 'rswfddp3bl')

data = [go.Scatter(x=df_joined['action_date'],y=df_joined['zero'],mode='markers',name='Markers and Text',text=df_joined['title'],textposition='bottom')]
py.iplot(data)


