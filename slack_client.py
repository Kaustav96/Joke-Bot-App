import requests
import json
from auth import DEFAULT_SLACK_WEBHOOK
from datetime import datetime
HEADERS = {
    'Content-type': 'application/json'
}
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
morningtime = now.replace(hour=6, minute=0, second=0, microsecond=0)
eveningtime = now.replace(hour=18, minute=0, second=0, microsecond=0)
afternoontime = now.replace(hour=12, minute=0, second=0, microsecond=0)
time4pm = now.replace(hour=16, minute=0, second=0, microsecond=0)
file_path = ''
if now < morningtime:
    file_path = 'gm.png'
if now > eveningtime:
    file_path = 'ge.png'
if afternoontime < now < time4pm:
    file_path = 'ga.png'
else:
    file_path = 'gm.png'

def slacker(webhook_url=DEFAULT_SLACK_WEBHOOK):
    def slackit(msg):
        payload = {'text': msg}

        return requests.post(webhook_url, headers=HEADERS, data=json.dumps(payload))

    return slackit


def slacker_file():
    def slackerfile():
        with open(file_path, 'rb') as f:
            payload = {"filename": file_path,
                       "token": "xoxp-1004629925682-1005947718707-1010298318019-b59ee7277766e2c1bc0d0467350e1b75",
                       "channels": "jokes"}
            requests.post("https://slack.com/api/files.upload", params=payload, files={'file': f})

    return slackerfile()
