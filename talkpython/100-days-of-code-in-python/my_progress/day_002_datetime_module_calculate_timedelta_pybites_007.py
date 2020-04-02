#!/usr/bin/env python
# -*- coding; utf-8 -*-

'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
from datetime import timedelta
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


def _convert_to_datetime(line):
    '''
    TODO 1:
    Given a log line extract its timestamp and convert it to a datetime object. 
    For example calling the function with:
        INFO 2014-07-03T23:27:51 supybot Shutdown complete.
    returns:
        datetime(2014, 7, 3, 23, 27, 51)
    '''
    timestamp = line.split()[1]
    parse_format = "%Y-%m-%dT%H:%M:%S"
    return datetime.strptime(timestamp, parse_format)


def time_between_shutdowns(loglines):
    '''
    TODO 2:
    Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
    timedelta between the first and last one. 
    Return this datetime.timedelta object.
    '''
    shutdown_events = []

    for line in loglines:
        if SHUTDOWN_EVENT in line:
            dtobj = _convert_to_datetime(line)
            shutdown_events.append(dtobj)

    time_diff = shutdown_events[-1] - shutdown_events[0]
    print(type(time_diff))
    return time_diff


print(time_between_shutdowns(loglines))
