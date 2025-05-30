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
  logger.info("Interval set to %ss", PING_INTERVAL)
  last_status = True  # Assume server is initially up

  while True:
    current_status = False
    timestamp = get_local_time()

    # Try pinging multiple times to confirm status
    retries = 0
    retry_interval = 10
    while retries < MAX_RETRIES and not current_status:
      current_status = is_server_reachable(PING_TO_IP)
      if not current_status:
        logger.warning("Ping failed at %s. Retrying in %ss (%s)",
                       timestamp, retry_interval, retries + 1)
        time.sleep(retry_interval)  # Wait before retrying
      else:
        logger.info("Ping ok! Time: %s", timestamp)
      retries += 1

    if current_status:
      if not last_status:
        # Server came back online
        log_online = f"Server {PING_TO_IP} is now reachable. Time: {timestamp}"
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


