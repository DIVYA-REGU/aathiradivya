from datetime import datetime
import pytz

def time_delta(t1, t2):
    dt_format = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, dt_format)
    dt2 = datetime.strptime(t2, dt_format)
    dt1_utc = dt1.astimezone(pytz.utc)
    dt2_utc = dt2.astimezone(pytz.utc)
    time_diff_seconds = abs((dt1_utc - dt2_utc).total_seconds())
    return int(time_diff_seconds)
t = int(input())
for _ in range(t):
    t1 = input().strip()
    t2 = input().strip()
    print(time_delta(t1, t2))
