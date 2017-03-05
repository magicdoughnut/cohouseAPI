import pandas as pd

# Read our backups back in..
df_companies = pd.read_pickle('companies.pkl')
df_fillings = pd.read_pickle('fillings.pkl')

# np_thing = df_fillings['title'].as_matrix()

# print df_fillings.head()

# np_thing = df_fillings['date'].as_matrix()
# print np_thing

df_officer_change = df_fillings.query("category == 'officers'")
df_joined =  pd.merge(df_officer_change, df_companies, on='company_number', how='left')[['title', 'action_date']]

print df_joined.head()
# np_thing = df_officer_change['title'].as_matrix()
