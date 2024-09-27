from datetime import datetime
def time_delta(date1, date2):
    format = '%a %d %b %Y %H:%M:%S %z'
    date = datetime.strptime(date1, format)
    date1 = datetime.strptime(date2, format)
    return int((date-date1).total_seconds())
