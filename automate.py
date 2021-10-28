import requests
import random
from super_secret import phone
import schedule

quotes_list = open("quotes.txt")
quotes = quotes_list.readlines()
quotes_list.close()
quote = 'Good morning, Grandpa! Here is the quote of the day: ' + (quotes[random.randint(0, len(quotes)-1)])

resp = requests.post('https://textbelt.com/text', {
    'phone': phone,
    'message': quote,
    'key': 'textbelt',
})

schedule.every().day.at("06:00").do(resp)

print(resp.json())
