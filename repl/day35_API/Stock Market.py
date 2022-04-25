"""
https://www.alphavantage.co/documentation/

TIME_SERIES_DAILY

This API returns raw (as-traded) daily time series (date, daily open, daily high, daily low, daily close, daily volume) of the global equity specified, covering 20+ years of historical data. If you are also interested in split/dividend-adjusted historical data, please use the Daily Adjusted API, which covers adjusted close values and historical split and dividend events.


API Parameters
❚ Required: function

The time series of your choice. In this case, function=TIME_SERIES_DAILY

❚ Required: symbol

The name of the equity of your choice. For example: symbol=IBM

❚ Optional: outputsize

By default, outputsize=compact. Strings compact and full are accepted with the following specifications: compact returns only the latest 100 data points; full returns the full-length time series of 20+ years of historical data. The "compact" option is recommended if you would like to reduce the data size of each API call.

❚ Optional: datatype

By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

❚ Required: apikey

Your API key. Claim your free API key here.
"""
import json
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "DG2ITFQ2H3QS668A"
time_series = "TIME_SERIES_DAILY"
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=DG2ITFQ2H3QS668A

parameters = {
    "function": time_series,
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
day_range = response.json()['Time Series (Daily)']
# print(day_range)
# This will print the last day of trading. In my case it was Aug-6 (Fri) and Aug-5 (Thur)
# Below logic works but I want to make the code more feature rich so that I don't have to enter dates.
# price_diff_between_stocks = float(response.json()['Time Series (Daily)']['2021-08-06']['4. close']) - float(response.json()['Time Series (Daily)']['2021-08-05']['4. close'])
# print(price_diff_between_stocks)
# print(response.json()['Time Series (Daily)']['2021-08-06']['4. close'])
index = 0
lst = []
for i in day_range:
    # print(response.json()['Time Series (Daily)'][i]['4. close'])
    lst.append(response.json()['Time Series (Daily)'][i]['4. close'])
    index = index + 1
    if index > 1:
        break

print("Price difference between last two days of stock is", float(lst[0]) - float(lst[1]))
# print(lst)
# diff_percent = (difference / yesterday's closing price) * 100
diff_percentage = (float(lst[0]) - float(lst[1]) / float(lst[0])) / 100
print("Difference in percentage ", float(diff_percentage))
if (float(diff_percentage) > 5.0):
    print("get news as the percentage is 5%")
