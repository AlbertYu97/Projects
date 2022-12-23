import requests
from datetime import date
from datetime import timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = " NC7UXWTCHV2WK05Z"
NEWS_API_KEY = "a003491688b54b60bd176cb2b8ad40ca"
account_sid = "AC75edd3862c92e023536814768b688986"
auth_token = "2ce9629f816007de661a27da574e0097"

# Find the price change of the stock
parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
stock_data = response.json()
stock_data_past_20days = stock_data["Time Series (Daily)"]
# Yesterday's and the day before yesterday's date
yesterday = str(date.today()-timedelta(days=1))
day_before_yesterday = str(date.today()-timedelta(days=2))

yesterday_end_price = float(stock_data_past_20days[yesterday]['4. close'])
day_before_yesterday_end_price = float(stock_data_past_20days[day_before_yesterday]['4. close'])
price_change = (yesterday_end_price-day_before_yesterday_end_price)/yesterday_end_price

# if abs(price_change) > 0.05:
#  If price change is greater than 5%, get the first 3 news pieces for the COMPANY_NAME.
today = str(date.today())
news_parameters = {
    "q": COMPANY_NAME,
    "from": yesterday,
    "to": today,
    "sortby": "relevancy",
    "apiKey": NEWS_API_KEY
}

news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
news_data_last3 = news_data['articles'][:3]

# Send seperate messages with the percentage change and each article's title and description to  phone number.
if price_change > 0:
    symbol = "🔺"
else:
    symbol = "🔻"
percentage = round(price_change*100)
client = Client(account_sid, auth_token)
for news in news_data_last3:
    message = client.messages \
        .create(
        body=f"TSLA: {symbol} {percentage}%\nHeadline: {news['title']}\nBrief: {news['description']} ",
        from_='+18475954584',
        to='+16476792872'
    )



