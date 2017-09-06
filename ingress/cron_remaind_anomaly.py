# coding:utf-8
# アノマリー開催日までの残日数を算出

from datetime import datetime
from .property import TIME_ZONE, ANOMARY_DAY

#現在の日付を取得(TimeZone起算)
now = datetime.now(TIME_ZONE)

print("anomary_day:" .format(ANOMARY_DAY))
print("now:".format(now))