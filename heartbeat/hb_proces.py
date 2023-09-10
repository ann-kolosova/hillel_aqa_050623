"""Logout data from hblog."""

import sys
from datetime import datetime, timedelta
from pathlib import Path

time_a = 30
time_b = 32

# find logger module
logger_file = Path(__file__).parent.parent / 'lesson_23'
sys.path.insert(0, str(logger_file))
from logger import logger

# find data file
hblog_file = Path(__file__).parent.parent / 'heartbeat' / 'hblog'

# open and read file
with open(hblog_file, mode='r') as f:
    lines = f.readlines()

# split each line and extract the time component
time_list = [line.split(' ')[10] for line in lines]

datetime_list = []

# convert unique time strings
for i in time_list:
    time_convert = datetime.strptime(i, '%H:%M:%S')
    datetime_list.append(time_convert)

# logout data
for i in range(len(datetime_list) - 1):
    time1_str = datetime_list[i].strftime('%H:%M:%S')
    time2_str = datetime_list[i + 1].strftime('%H:%M:%S')
    delta = datetime_list[i] - datetime_list[i + 1]
    if timedelta(seconds=time_a) < delta < timedelta(seconds=time_b):
        logger.warning(f'{time1_str}, {time2_str}, {delta}')
    elif delta >= timedelta(seconds=time_b):
        logger.error(f'{time1_str}, {time2_str}, {delta}')
