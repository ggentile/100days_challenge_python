import requests
from datetime import datetime
import smtplib


MY_LAT = -23.8288896
MY_LONG = -46.8123648

EMAIL = ""
PASSWD = ""

message = ""


def is_iss_overhead():
    global message
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()

    data_iss = response_iss.json()

    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])
    if (MY_LAT - 5) <= iss_latitude >= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude >= (MY_LONG + 5):
        message = f"Hey, the ISS is going close by you, and it has longitude: {iss_longitude}\nlatitude: {iss_latitude}"
        return message, True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    current_datetime = datetime.now()
    current_hour = current_datetime.hour

    if current_hour >= sunset or current_hour <= sunrise:
        return True


if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f"Subject:LookUp to the sky!\n\n{message}")
