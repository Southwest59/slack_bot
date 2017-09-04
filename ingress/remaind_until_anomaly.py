#アノマリー開催日までの残日数を算出
# coding:utf-8

from datetime import datetime,timedelta
import pytz

def remaind_until_anomaly():

    #anomary開催日
    anomary_day = "2017/11/04"

    #TimeZone設定
    timezone = pytz.timezone('Asia/Tokyo')

    #現在の日付
    now = datetime.now(tz=timezone)

    print("NowDate:" + now)