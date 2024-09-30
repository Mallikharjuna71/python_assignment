from datetime import datetime


def date_name(n):
    date = datetime.strptime(n, '%m %d %Y')
    name = datetime.strftime(date, '%A')
    return name
