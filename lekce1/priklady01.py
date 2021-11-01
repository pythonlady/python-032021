import pandas
import requests
import numpy
r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/titanic.csv")
open("titanic.csv", 'wb').write(r.content)
df_titanic = pandas.read_csv("titanic.csv")
#print(df_titanic.columns)
df_titanic_pivot = pandas.pivot_table(df_titanic, index=["Pclass", "Sex"], columns="Survived", values="Name", aggfunc=len, margins=True)
print(df_titanic_pivot)

import requests
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