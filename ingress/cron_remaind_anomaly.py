# coding:utf-8
# アノマリー開催日までの残日数を算出

from datetime import date,datetime,timezone,timedelta

#Constants
ANOMARY_DAY = date(2017,11,4)   #アノマリー開催日

#残日数算出
try:
    today = date.today()
    msg_rtn = ''

    if ANOMARY_DAY > today:
        remaind = abs(ANOMARY_DAY - today)

        msg_rtn = 'おはようございます。'
        msg_rtn += '大阪アノマリーまであと' + str(remaind.days) + '日です。'

        print(msg_rtn)

#elif ANOMARY_DAY == today:

#else:

except Exception as e:
    print(e)
    raise e
