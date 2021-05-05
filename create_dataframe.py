import pandas as pd

data = {"name": ["revanth"], "time": ["1998-11-30"], "event_type": ["birthday"]}

df = pd.DataFrame(data, columns=["name", "time", "event_type"])
# df['name']=revanth

# df['time']=1998-11-30

# df['event_type']=birthday
print(df.head())
print(df.columns)

df.to_csv("events_log.csv", header=None, index=None)
