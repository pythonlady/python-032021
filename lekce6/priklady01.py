import requests
import pandas
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import mannwhitneyu

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/psenice.csv") as r:
  open("psenice.csv", 'w', encoding="utf-8").write(r.text)

df = pandas.read_csv("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/psenice.csv")

x = df["Rosa"]
y = df["Canadian"]
print(x.shape)
print(y.shape)
print(mannwhitneyu(x, y))
print(binom.pmf(k=len(x), n=len(x), p=0.5) + binom.pmf(k=0, n=len(x), p=0.5))