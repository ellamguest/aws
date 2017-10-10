import pandas as pd
df = pd.read_csv('/Users/emg/Programming/GitHub/sub-text-analysis/raw-data/td_comments_2017_05.csv')

author_counts = df.groupby('author')['created_utc'].count()
author_counts.describe()

df['date'] = pd.to_datetime(df['created_utc'],unit='s')
df['month'] = list(zip(df['date'].dt.month, df['date'].dt.year))
df.index=df['date']

m_comments = df.groupby(pd.TimeGrouper(freq='M'))['created_utc'].count()
m_authors = df.drop_duplicates(['author','month']).groupby(pd.TimeGrouper(freq='M'))['created_utc'].count()

output = pd.DataFrame({'comments':m_comments, 'authors':m_authors})
