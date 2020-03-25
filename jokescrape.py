import requests
import json
import pymongo
import time
import logging
from slack_client import slacker
from slack_client import slacker_file
import schedule
import self as self
from datetime import datetime


my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["jokes_api"]
FILE_NAME = 'yo_mama_jokes.json'
FILE_NAME1 = 'chuck_norris_jokes.json'
FORMAT = '[%(asctime)-15s] %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG, filename='bot.log', filemode='a')


def save_json_mama_joke(x):
    with open(FILE_NAME, 'a') as f:
        json.dump(x, f)


def save_json_chuck_norris_joke(x):
    with open(FILE_NAME1, 'a') as f:
        json.dump(x, f)


try:

    def main_jokes():
        def yoMamaJokeApi():
            res = requests.get('https://api.yomomma.info/')
            # soup = BeautifulSoup(res.text, 'html.parser')
            joke = json.loads(res.text)
            yo_mama_joke = joke['joke']
            save_json_mama_joke(joke)
            mycol = my_db["yo_mama_jokes"]
            mydict = {'joke': joke['joke']}
            x = mycol.insert_one(mydict)
            logging.warning('Joke added to DB - Yo Mama')
            return yo_mama_joke

        def chuckNorrisJokeApi(self):
            res1 = requests.get('http://api.icndb.com/jokes/random')
            # soup1 = BeautifulSoup(res1.text, 'html.parser')
            joke1 = json.loads(res1.text)
            chuck_norris_joke = joke1['value']['joke']
            mycol = my_db["chuck_norris_joke"]
            mydict = {'joke': joke1['value']['joke']}
            x = mycol.insert_one(mydict)
            logging.warning('Joke added to DB - Chuck Norris')
            save_json_chuck_norris_joke(joke1['value'])
            return chuck_norris_joke

        yo_mama_joke = yoMamaJokeApi()
        chuck_norris_joke = chuckNorrisJokeApi(self)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print('Sent jokes to the Slack App - ', dt_string)
        slacker_file()
        logging.warning('Attachment has been sent to slack')
        slack_text = f'Sending 2 Jokes to make your day more cheerful and full of happiness -\n\nJoke 1 - \n{yo_mama_joke}.\nJoke 2 -\n{chuck_norris_joke}. '
        slacker()(slack_text)
        logging.warning('Jokes sent to slack channel #jokes')
        logging.warning(yo_mama_joke + ", "+chuck_norris_joke)
        # sending email
        # sending email
        # with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        #     smtp.ehlo()  # identifies with mail server we are using
        #     smtp.starttls()  # encrypt our traffic
        #     smtp.ehlo()  # again run this to reidetify as encrypted connection
        #
        #     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        #     subject = 'Jokes Mail'
        #     msg = f'Subject :{subject}\n\n{yo_mama_joke}\n\n{chuck_norris_joke}'
        #
        #     smtp.sendmail(EMAIL_ADDRESS, 'kaustavbanerjee96@gmail.com', msg)
        #
        #     # mqntilwxhmchhfas

    main_jokes()

except Exception as e:
    slacker()(f'Exception occurred: [{e}]')
    logging.error(e)
    print(f'Exception occurred as {e}')


schedule.every().day.at("20:00").do(main_jokes)  # send jokes at night 8
schedule.every().day.at("08:00").do(main_jokes)  # send jokes at morning 8
while 1:
    # Checks whether a scheduled task
    # is pending to run or not
    # print("Current time ran job at - ",time.time())
    schedule.run_pending()
    time.sleep(1)
