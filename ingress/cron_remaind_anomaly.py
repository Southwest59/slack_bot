# coding:utf-8
# アノマリー開催日までの残日数を算出

import boto3
import json
import logging
import os

from base64 import b64decode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from datetime import date,datetime,timezone,timedelta


logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Slack の設定
SLACK_POST_URL = os.environ['slackPostURL']
SLACK_CHANNEL = os.environ['slackChannel']

response = boto3.client('cloudwatch', region_name='ap-northeast-1')

#アノマリー開催日
ANOMARY_DAY = date(2017,11,4)

def build_message():
    #残日数算出
    try:
        today = date.today()
        msg = ''

        if ANOMARY_DAY > today:
            remaind = abs(ANOMARY_DAY - today)

            msg = "おはようございます。"
            msg += "\n大阪アノマリーまであと" + str(remaind.days) + "日です。"

            #print(msg)

        elif ANOMARY_DAY == today:
            msg = "おはようございます。"
            msg += "\n大阪アノマリー当日です、Go!ENL!!"
        else:
            msg = "大阪アノマリーは終わったyo"

        payload = {'text' :msg}
        return payload

    except Exception as e:
        print(e)
        raise e

def lambda_handler(event, context):
    content = build_message()

    # SlackにPOSTする内容をセット
    slack_message = {
        'channel': SLACK_CHANNEL,
        "attachments": [content],
    }

    # SlackにPOST
    try:
        req = Request(SLACK_POST_URL, json.dumps(slack_message).encode('utf-8'))
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", slack_message['channel'])
    except Exception as e:
        logger.error("Request failed: %s", e)

