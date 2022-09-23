import pandas as pd
import calendar
import datetime

def index_logic(index):
    if index not in [5, 6]:
        return True
    return False

def read_sleep_file(filename):
    ff = pd.read_csv(filename, skiprows=lambda x: index_logic(x), delimiter=',')
    return ff

def UTC2epoch(x):
    timestamp = pd.Timestamp(x)
    epoch = calendar.timegm(timestamp.utctimetuple())
    #e = datetime.datetime(1970, 1, 1, 0, 0)
    #t = x #datetime.datetime(year, month, day, hour, minute)
    #return (t-e).total_seconds()
    return epoch
  
def read_hr_file(filename):
    ff = pd.read_csv(filename, skiprows=5, delimiter=',')
    return ff