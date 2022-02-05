import requests
from news_sec import get_news
from send_mail import sending_email

COMPANY = "TSLA"

response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={COMPANY}&apikey=")
response.raise_for_status()
data = response.json()
full_week_data = data['Time Series (Daily)'].items()
last_two_date = list(full_week_data)[1:3]
price_closed_prev = float(last_two_date[1][1]['4. close'])
price_opened_yes = float(last_two_date[0][1]['4. close'])

variant_noabs = round((price_opened_yes - price_closed_prev), 2)
total_dif = round(abs(price_opened_yes - price_closed_prev), 2)
variance = round((total_dif / price_opened_yes) * 100, 2)

if total_dif > 5:
    news = get_news()
    sending_email(variant_noabs, news)

