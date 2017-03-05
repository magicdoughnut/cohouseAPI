import requests
import pandas as pd
import numpy as np

mark_auth = ('5udJ0dC3FWn2CYuuWW680oByNaxYDK5nDyhPqrex', '')

def get_companies(query_string, items_per_page, start_index):
	request_url = 'https://api.companieshouse.gov.uk/search/companies?q={}&items_per_page={}&start_index={}'.format(
		query_string,
		items_per_page,
		start_index,
	)
	print request_url
	r = requests.get(request_url, auth=mark_auth)
	# Hopefully this will pass
	try:
		return r.json()
	# ...but if not then prict out the json to see what the error was
	except:
		print r, r.text, str(r)
		exit()

def get_filing_history(company_number):
	r = requests.get(
		'https://api.companieshouse.gov.uk/company/{}/filing-history'.format(
			company_number
		),
		auth=mark_auth
	)
	return r.json()	

jdata = get_companies('solar', 10, 10)
total_results = jdata['total_results']
# for i in jdata:
	# if i == 'items':
		# print i + '= Look into variable'
	# else:
		# print i + '=',jdata[i]

# exit()

page_size = 50
df_companies = None
# for i in xrange(1, total_results, page_size):
for i in range(1,300,50):
	print i
	jdata = get_companies('solar', page_size, i)
	new_companies = pd.DataFrame(jdata['items'])
	# print new_companies['title']
	# This will happen for the first one only - make a new dataframe
	if df_companies is None:
		df_companies = pd.DataFrame(new_companies)
	# This will happen all the other times - append to the dataframe
	else:
		df_companies = df_companies.append(new_companies, ignore_index=True)
		# df_fillings = pd.concat(df_fillings, new_filling)

# print jdata.keys()
# print jdata['items'][0].keys()
# exit()


# df_companies = pd.DataFrame(jdata['items'])
# print df_companies[['company_number', 'title']].head()
# print df_companies['company_number'].tolist()
# print df_companies['company_number'].as_matrix()
# print df_companies['company_number'].nunique()

df_fillings = None

for row_index, row in df_companies.iterrows():
	if 'solar' in row['title'].lower():
		print row_index, row['company_number'], row['title']
		jdata = get_filing_history(row['company_number'])
		if 'items' in jdata:
			print jdata['items']
			new_filling = pd.DataFrame(jdata['items'])

			# How to add a new column
			# Here we want each filing to know which company filed it
			# (basically linking the two tables)
			new_filling['company_number'] = row['company_number']

			# print new_filling.head()
			# print new_filling.tail()
			# print new_filling

			# This will happen for the first one only - make a new dataframe
			if df_fillings is None:
				df_fillings = pd.DataFrame(new_filling)
			# This will happen all the other times - append to the dataframe
			else:
				df_fillings = df_fillings.append(new_filling, ignore_index=True)
				# df_fillings = pd.concat(df_fillings, new_filling)

		# DONT DO THIS!
		# category_store = []
		# date_store = []
		# dsecription_store = []
		# for row_index,row2 in df2.iterrows():
			# print row2['category'], row2['date'], row2['description']
			# category_store.append(row2['category'])
			# date_store.append(row2['date'])
			# dsecription_store.append(row2['description'])

# How many companies do we have fillings for?  We want unique company_number's
# print df_fillings['company_number'].nunique()
# print df_fillings.shape
# print df_fillings.head()

# Get all the options for category
# print df_fillings['category'].unique()

# Get me all the fillings which have category = 'officers'
df_officer_change = df_fillings.query("category == 'officers'")

# But we only want to see two columns: date and company numbers
# print df_officer_change[['company_number', 'action_date']]

# You can do joins on stuff in pandas too.  Cos we actually want the company title (not the company_number)
# print pd.merge(df_officer_change, df_companies, on='company_number', how='left')[['title', 'action_date']]


# Backup everything
df_companies.to_pickle('companies.pkl')
df_fillings.to_pickle('fillings.pkl')

# Read our backups back in..
# df_companies = pd.read_pickle('lol.pkl')
# df_fillings = pd.read_pickle('lol2.pkl')

# # Get a specific company...
# jack = df_companies.query("title == 'SOLAR ADVANCED SYSTEMS LTD'")
# # Get all the fillings for that company
# print df_fillings.query("company_number == {}".format(jack['company_number']))

# If you wanna do plotting etc. you can drop back to numpy using
np_thing = df_companies['company_number'].as_matrix()
py_thing = df_companies['company_number'].tolist()

exit()





# df.to_pickle('backup_data.pkl')
# pd.read_pickle('backup_data.pkl')
# exit()




print '\n'
for i in jdata:
	if i == 'items':
		print i + ' length =',len(jdata[i])
	else:
		print i + '=',jdata[i]

print '\n'
items = jdata['items']
items = items[0]
print 'no of items = ',len(items)
for item in items:
	print item,'=',items[item]
print '\n'



# import json
# import requests

# payload = {'key': '5udJ0dC3FWn2CYuuWW680oByNaxYDK5nDyhPqrex'}

# r = requests.get('https://api.companieshouse.gov.uk/search/companies?q=solar&items_per_page=2&start_index=1', auth=('5udJ0dC3FWn2CYuuWW680oByNaxYDK5nDyhPqrex', ''))

# jdata = r.json()


# print '\n'
# print '\n'
# for i in jdata:
# 	if i == 'items':
# 		print i + ' length =',len(jdata[i])
# 	else:
# 		print i + '=',jdata[i]

# print '\n'
# print '\n'
# items = jdata['items']
# items = items[0]
# print 'no of items = ',len(items)
# for item in items:
# 	print item,'=',items[item]
# print '\n'
# print '\n'



# # GET https://api.companieshouse.gov.uk/company/{company_number}/filing-history




