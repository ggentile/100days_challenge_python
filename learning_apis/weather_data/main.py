import requests
from twilio.rest import Client

api_key = ""
web_url = ""

account_sid = ""
auth_token = ""

weather_params = {
    "lat": -20.846704,
    "lon": -41.120220,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

my_list = []

response = requests.get(web_url, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️ ",
        from_='',
        to=''
    )
    print(message.status)
