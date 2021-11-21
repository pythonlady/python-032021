import requests
import pandas
import numpy
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import mannwhitneyu


with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)
air_polution = pandas.read_csv("air_polution_ukol.csv")
#print(air_polution)
air_polution["date"] = pandas.to_datetime(air_polution["date"])
#print(air_polution.dtypes)
air_polution["month"] = air_polution["date"].dt.month
air_polution["year"] = air_polution["date"].dt.year
#print(air_polution)

#H0: Průměrný počet částic je stejný pro oba roky.
#H1: Průměrný počet částic je vyšší pro rok 2020.

air_polution_month = air_polution[air_polution["month"] == 1]
air_polution_month = air_polution.dropna()
print(air_polution_month.dtypes)
print(air_polution_month)


x = air_polution_month[air_polution_month["year"] == "2020"]["pm25"]
y = air_polution_month[air_polution_month["year"] == "2019"]["pm25"]
mannwhitneyu(x, y, alternative="greater")
