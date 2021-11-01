import pandas
import requests
import numpy
r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/titanic.csv")
open("titanic.csv", 'wb').write(r.content)
df_titanic = pandas.read_csv("titanic.csv")
#print(df_titanic.columns)
df_titanic_pivot = pandas.pivot_table(df_titanic, index=["Pclass", "Sex"], columns="Survived", values="Name", aggfunc=len, margins=True)
print(df_titanic_pivot)

