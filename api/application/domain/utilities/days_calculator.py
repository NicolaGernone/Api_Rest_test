import datetime

def days_range(start, end):
    date_format = "%m/%d/%Y"
    a = datetime.strptime('8/18/2008', date_format)
    b = datetime.strptime('9/26/2008', date_format)
    delta = b - a
    return delta.days