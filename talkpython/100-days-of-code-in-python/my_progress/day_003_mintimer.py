#! /usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta
import os
import sys

minutes = sys.argv[1]

try:
    minutes = int(minutes)
except:
    sys.exit(print("Enter an integer in minutes when issuing the command.\n"
                   "\tEx: 'python day_003_mintimer.py 60'"))

start = datetime.now()
end = start + timedelta(minutes=minutes)

while datetime.now() < end:
    continue

if datetime.now() > end:
    beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
    beep(6)

