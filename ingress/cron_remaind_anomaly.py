# coding:utf-8
# アノマリー開催日までの残日数を算出

from datetime import date,datetime,timezone,timedelta

#Constants
ANOMARY_DAY = date(2017,11,4)   #アノマリー開催日
MSG_REMAIND_JP = ''
MSG_REMAIND_EN = ''

#残日数算出
try:
    today = date.today()
    msg_rtn = ''

    if ANOMARY_DAY > today:
        day = abs(ANOMARY_DAY - today)
        print(remaind)
#    elif ANOMARY_DAY == today:
#    else:

except Exception as e:
    print(e)
    raise e
