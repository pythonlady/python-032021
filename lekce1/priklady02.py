import requests
import pandas
import numpy

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/london_merged.csv")
open("london_merged.csv", 'wb').write(r.content)
df_london = pandas.read_csv("london_merged.csv")
#print(df_london)
#print(df_london.columns)
#print(df_london["weather_code"])
df_london["timestamp"] = pandas.to_datetime(df_london["timestamp"])
#print(df_london.dtypes)
df_london["year"] = df_london["timestamp"].dt.year
#print(df_london["year"])
df_london_index = df_london.reset_index()
#print(df_london_index)
df_london_index_pivot = pandas.pivot_table(df_london_index, index="weather_code", columns="year", values="index",
                                             aggfunc=numpy.count_nonzero)
#df_london_grouped = df_london_grouped["weather_code"]
print(df_london_index_pivot)