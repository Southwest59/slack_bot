# アノマリー開催日までの残日数を算出
# coding:utf-8

from datetime import datetime, timedelta
import pytz

ANOMARY_DAY = '2017/11/04'

# TimeZone設定
timezone = pytz.timezone('Asia/Tokyo')

# 現在の日付
now = datetime.now(tz=timezone)
remaind_day = ANOMARY_DAY - now

#print("NowDate:" + now)
#print('NowDate:' + datetime.now(tz=timezone))
