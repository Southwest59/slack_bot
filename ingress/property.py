# coding:utf-8

from datetime import date
import pytz

#TimeZone
TIME_ZONE = pytz.timezone('Asia/Tokyo')

#アノマリー開催日
ANOMARY_DAY = date(2017,11,4)

#現在
#TODAY = date.today(TIME_ZONE)


#test
print( 'Anomary_day:' + date.strftime(ANOMARY_DAY,'%y-%m-%d') )
print( TIME_ZONE)