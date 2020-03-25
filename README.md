# Jokes Slackbot App


![Jokes SlackBot App](https://github.com/Kaustav96/python-jokes-app/blob/master/slackbot-jokes-app.jpg)

## Features
- Sit back & relax - you will get 2 jokes daily in the morning as well as night.
- Get Slack Notification
- Depending upon time of day the image will be changing and send to slack with the jokes.
- Jokes are coming from 2 API's that are famous for giving random jokes.
- The Jokes from the APi's are stored in database also. (DB used - MongoDB)
- Its ROBUST! 
  - What if script fails?
  - You get Slack notifications about the exceptions too.
  - You have log files (check `bot.log`) too, to evaluate what went wrong

## Installation
- You need Python.
- You need MongoDB installed.
  -Follw steps from the link provided to install MomgoDB. (https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/)
- You need a Slack account + Slack Webhook to send slack notifications to your account.
- Install dependencies by running
```bash
pip install pymongo
pip install requests
pip install beautifulsoup4
```
- Clone this repo and create auth.py
```bash
git clone https://github.com/Kaustav96/Joke-Bot-App.git
cd Joke-Bot-App
touch auth.py
```
- Write your Slack Webhook into auth.py
```python
DEFAULT_SLACK_WEBHOOK = 'https://hooks.slack.com/services/<your custome webhook url>'
```
