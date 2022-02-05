import requests

COMPANY_NAME = "Tesla Inc"

parameters = {
    "totalResults": 3,
    "language": "en",
}


def get_news():
    response = requests.get(f"https://newsapi.org/v2/everything?q={COMPANY_NAME}"
                            f"&apiKey=", params=parameters)
    response.raise_for_status()
    data = response.json()
    last_news = data['articles']
    three_last_news = last_news[:3]
    title = [values['title'] for values in three_last_news]
    brief = [values['description'] for values in three_last_news]
    manchete = [x+y for x in title for y in brief]
    return manchete[0]
