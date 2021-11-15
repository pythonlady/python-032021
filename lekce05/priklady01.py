mport pandas
import statistics
import seaborn
import numpy
import matplotlib.pyplot
import requests

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)

df = pandas.read_csv("crypto_prices.csv")
print(df)


df_grouped = df.groupby("Name")["Close"]
print(df_grouped)


df_grouped_change["Close_change"] = df_grouped["Close"].pct_change()
print(df_grouped_change)