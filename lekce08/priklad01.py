import requests
import pandas
import seaborn
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import yfinance as yf


csco = yf.Ticker("CSCO")
csco_df = csco.history(period="1y")
#print(csco_df.describe())
#print(csco_df.columns)
#print(csco_df)

#1)
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(csco_df["Close"])
plt.show()

#2)
from statsmodels.tsa.ar_model import AutoReg

model = AutoReg(csco_df['Close'], lags=20, trend="t", seasonal=True, period=12)
model_fit = model.fit()
predictions = model_fit.predict(start=csco_df.shape[0], end=csco_df.shape[0] + 5)
df_forecast = pandas.DataFrame(predictions, columns=["Prediction"])
df_with_prediction = pandas.concat([csco_df, df_forecast])
df_with_prediction[["Close", "Prediction"]].tail(100).plot()
plt.show()

#3)
from statsmodels.tsa.holtwinters import ExponentialSmoothing
mod = ExponentialSmoothing(csco_df["Close"], seasonal_periods=100, trend="add", seasonal="add", use_boxcox=True, initialization_method="estimated",)
res = mod.fit()
csco_df["HM"] = res.fittedvalues
csco_df[["HM", "Close"]].plot()

csco_df_forecast = pandas.DataFrame(res.forecast(64), columns=["Prediction"])
csco_df_with_prediction = pandas.concat([csco_df, csco_df_forecast])
csco_df_with_prediction[["Close", "Prediction"]].plot()
plt.show()


