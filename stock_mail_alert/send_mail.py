import smtplib

MY_EMAIL = 'mrgiannitest@gmail.com'
PASSWD = ''
UP = "🔺"
DOWN = "🔻"


def sending_email(percentage, news):
    if percentage < 0:
        separator = news.split('- ')
        message = f"Subject:{separator[0]}\n\nTSLA: {DOWN}{percentage}%\n{separator[1]}"
    else:
        message = f"Subject:{news[0]}\n\nTSLA: {UP}{percentage}%\n{news[1]}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=message.encode('utf-8'))
