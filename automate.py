import requests
import random # to pick a random quote
from super_secret import phone # hidden grandpa's phone number from you scammy Sammies
import schedule # this will make the task wait until a certain time. Google python schedule library for more
import time
from datetime import datetime

# reading from the quotes txt which makes an array. Then concatenating my good morning string, the day of the week, and a randomly selected quote
quotes_list = open("quotes.txt")
quotes = quotes_list.readlines()
quotes_list.close()
today = (datetime.today().strftime('%A'))
quote_of_the_day = (quotes[random.randint(0, len(quotes)-1)])
quote = 'Good morning, Grandpa! Happy ' + today + '! Here is the quote of the day: ' + quote_of_the_day

# textbelt allows one text a day. simply import requests and add the following 5 lines of code. print(resp.json()) will trigger the post method
resp = requests.post('https://textbelt.com/text', {
    'phone': phone,
    'message': quote,
    'key': 'textbelt', # add _test to the end of textbelt to test without needing to use up a text
})

# put json response into a function so as to incorporate it into schedule method
def send_it():
    print(resp.json())

schedule.every().day.at("07:30").do(send_it) # let grandpa know we get up real early like an adult

while True:
    # Checks whether a scheduled task is pending to run or not
    schedule.run_pending()
    time.sleep(1)
