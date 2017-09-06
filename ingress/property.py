# coding:utf-8

from datetime import date,timedelta
from pytz import timezone

#TimeZone
TIME_ZONE = timezone('Asia/Tokyo')

#アノマリー開催日
ANOMARY_DAY = date(2017,11,4)

#test
print( 'Anomary_day:' + date.strftime(ANOMARY_DAY,'%y-%m-%d') )