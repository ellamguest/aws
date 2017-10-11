import pandas as pd
from datetime import datetime

print('GETTING SAMPLE DATA...')
df = pd.read_csv('td_all_authors.csv')

print()
print('THE SAMPLE DATA LOOKS LIKE...')
print(df.head())

print()
print('PREPPING TIME VARIABLES...')
df['date'] = pd.to_datetime(df['created_utc'],unit='s')
df['month'] = list(zip(df['date'].dt.month, df['date'].dt.year))
df.index=df['date']
print(df.head())

print()
print('GETTING MONTHLY COMMENT AND AUTHOR COUNTS...')
m_comments = df.groupby(pd.TimeGrouper(freq='M'))['created_utc'].count()
m_authors = df.drop_duplicates(['author','month']).groupby(pd.TimeGrouper(freq='M'))['created_utc'].count()

output = pd.DataFrame({'comments':m_comments, 'authors':m_authors})

print()
print('THE MONTHLY COUNTS ARE...')
print(output)

print()
print('SAVING OUTPUT...')
output.to_csv('output-{}.csv'.format(datetime.utcnow().strftime('%Y-%m-%d')))

print()
print('DONE!')
print()
