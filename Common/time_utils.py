import calendar
from datetime import datetime, timedelta


def get_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_date_number():
    return datetime.now().strftime('%Y-%m-%d')


def format_time(time_str, today=False):
    time_list = time_str.split('/')
    # XP上的时间是以-分割的
    if len(time_list) < 3:
        time_list = time_str.split("-")

    # 有时候年份会在以后一个,如：03-25-2016，此时查询数据将出错，因此要判断一下
    if len(time_list[2]) == 4:
        mon = time_list[0]
        day = time_list[1]
        time_list[0] = time_list[2]
        time_list[1] = mon
        time_list[2] = day

    time_str = ""
    for t in time_list:
        if len(t) < 2:
            t = "0" + t
        time_str += t + "-"
    time_str = time_str[:-1]
    if today:
        time_str += " 23:59:59"
    else:
        time_str += " 00:00:00"
    return time_str


def get_this_day(split='/') -> dict:
    today = datetime.now().strftime('%Y{}%m{}%d'.format(split, split))
    period = {'start_time': today,
              'end_time': today}

    return period


def get_this_week(split='-') -> dict:
    now = datetime.now()
    day_in_week = timedelta(days=now.isoweekday())
    day_from = now - day_in_week + timedelta(days=1)
    day_to = now - day_in_week + timedelta(days=7)
    period = {'start_time': day_from.strftime('%Y{}%m{}%d'.format(split, split)),
              'end_time': day_to.strftime('%Y{}%m{}%d'.format(split, split))}

    return period


def get_this_month(split='-') -> dict:
    now = datetime.now()
    year = now.year
    month = now.month
    last_day_of_month = calendar.monthrange(year, month)[1]
    month = str(month).rjust(2, '0')
    start_time = '{}{}{}{}{}'.format(year, split, month, split, "01")
    end_time = '{}{}{}{}{}'.format(year, split, month, split, last_day_of_month)
    period = {'start_time': start_time,
              'end_time': end_time}
    return period


def get_this_year(split='-'):
    now = datetime.now()
    start_time = '{}{}{}{}{}'.format(now.year, split, "01", split, "01")
    end_time = '{}{}{}{}{}'.format(now.year, split, "12", split, "31")
    period = {'start_time': start_time,
              'end_time': end_time}
    return period
