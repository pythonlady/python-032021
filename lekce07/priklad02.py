import requests
import pandas
import seaborn
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Fish.csv")
with open("Fish.csv", "wb") as f:
  f.write(r.content)

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Concrete_Data_Yeh.csv")
with open("Concrete_Data_Yeh.csv", "wb") as f:
  f.write(r.content)

df = pandas.read_csv("Fish.csv")
print(df)

#1) model je velice kvalitní
mod = smf.ols(formula="Weight ~ Length2", data=df)
res = mod.fit()
print(res.summary())

#2) model je o pár procent kvalitnější
mod = smf.ols(formula="Weight ~ Length2 + Height", data=df)
res = mod.fit()
print(res.summary())

# 3)
prumery = df.groupby("Species")["Weight"].mean()
df['species_prumerna_vaha'] = df['Species'].map(prumery)
mod = smf.ols(formula="Weight ~ Length2 + Height + species_prumerna_vaha", data=df)
res = mod.fit()
print(res.summary())
