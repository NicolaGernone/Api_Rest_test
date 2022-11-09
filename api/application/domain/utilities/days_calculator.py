import datetime

def days_range(start: datetime, end: datetime):
    """ Calulate the day between the start date and the end date"""
    delta = end - start
    return delta.days