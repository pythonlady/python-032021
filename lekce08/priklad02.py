import requests
import requests
import pandas
import seaborn
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/MLTollsStackOverflow.csv")
with open("MLTollsStackOverflow.csv", "wb") as f:
  f.write(r.content)

df = pandas.read_csv("MLTollsStackOverflow.csv")
print(df)

#1)
from statsmodels.tsa.seasonal import seasonal_decompose
decompose = seasonal_decompose(df['python'], model='multiplicative', period=12)
decompose.plot()
plt.show()

#2)
from statsmodels.tsa.holtwinters import ExponentialSmoothing
mod = ExponentialSmoothing(df["python"], seasonal_periods=12, trend="add", seasonal="add", use_boxcox=True, initialization_method="estimated",)
res = mod.fit()
df["HM"] = res.fittedvalues
df[["HM", "python"]].plot()

df_forecast = pandas.DataFrame(res.forecast(12), columns=["Prediction"])
df_with_prediction = pandas.concat([df, df_forecast])
df_with_prediction[["python", "Prediction"]].plot()
plt.show()

