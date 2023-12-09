import time

def time_now():
    (year, month, month_day, hours, minutes, seconds, weekday, yearday) = time.localtime()
    return f"{hours}:{minutes}:{seconds}"

def msg(message):
    print(f"[{time_now()}]\t{message}")
