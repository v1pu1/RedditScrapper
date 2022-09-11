import pandas as pd

df = pd.read_csv('subreddits-csv/dankmemes.csv')
print(df['url'])

for ind in df.index:
    data = df['url'][ind].split(",")
    print(data)