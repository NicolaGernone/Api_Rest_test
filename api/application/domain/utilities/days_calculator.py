import datetime
from functools import cached_property

def days_range(start: datetime, end: datetime):
    delta = end - start
    return delta.days