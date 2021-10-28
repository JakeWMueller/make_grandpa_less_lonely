import random
import schedule
import time
from twilio.rest import Client
from twilio_credentials import cellphone, twilio_account, twilio_number, twilio_token


quotes_list = open("quotes.txt")
quotes = quotes_list.readlines()
quotes_list.close()


def send_message(quotes):
    account = twilio_account
    token = twilio_token
    client = Client(account,token)
    quote = quotes[random.randint(0, len(quotes)-1)]

    client.messages.create(to=cellphone,
                        from_=twilio_number,
                        body= print("Good morning, Grandpa! Here is today's quote: " + quote))

schedule.every().day.at("06:00").do(send_message, quotes)
