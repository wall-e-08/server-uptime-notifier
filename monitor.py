import os
import subprocess
import time
from notifier import send_notification
from utils import is_valid_ipv4, get_local_time
import logging


logger = logging.getLogger(__name__)

PING_TO_IP = os.getenv("PING_TO_IP", "")
PING_INTERVAL = int(os.getenv("PING_INTERVAL_IN_SECONDS", "3600"))
MAX_RETRIES = 3  # Number of ping attempts before declaring failure


def is_server_reachable(ip: str) -> bool:
  try:
    # Ping with 1 attempt, timeout after 2 seconds
    result = subprocess.run(['ping', '-c', '1', '-W', '2', ip],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            timeout=5)
    return result.returncode == 0
  except:
    return False


def monitor_server():
  if not is_valid_ipv4(PING_TO_IP):
    logger.critical("Wrong ipv4 pattern! Found: `%s`!", PING_TO_IP)
    return
  last_status = True  # Assume server is initially up

  while True:
    current_status = False
    retries = 0

    # Try pinging multiple times to confirm status
    while retries < MAX_RETRIES and not current_status:
      current_status = is_server_reachable(PING_TO_IP)
      if not current_status:
        time.sleep(10)  # Wait 10 seconds before retrying
      retries += 1

    timestamp = get_local_time()

    if current_status:
      if not last_status:
        # Server came back online
        log_online = f"Server {PING_TO_IP} is now reachable as of {timestamp}"
        logger.info(log_online)
        send_notification("Server Status Alert", log_online)
    else:
      logger.warning("Server %s is not reachable at %s", PING_TO_IP, timestamp)
      if last_status:
        # Server went offline
        log_unreachable = f"Server {PING_TO_IP} became unreachable at {timestamp}"
        logger.warning(log_unreachable)
        send_notification("Server Status Alert", log_unreachable)

    last_status = current_status
    time.sleep(PING_INTERVAL)


