import os
import re
from datetime import datetime
import pytz


def get_local_time(time_format: str="%I:%M:%S %p, %d %B %Y ") -> str:
  tz = os.getenv("TZ", "Europe/London")
  time_pytz = pytz.timezone(tz)
  now_time = datetime.now(time_pytz)
  return now_time.strftime(time_format)

def is_valid_ipv4(ip: str) -> bool:
  pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
  return bool(re.fullmatch(pattern, ip))
