from dotenv import load_dotenv
load_dotenv()

import logging
import sys

from logger import init_configure_logging
from monitor import monitor_server
from utils import get_local_time

if __name__ == '__main__':
  init_configure_logging()
  logger = logging.getLogger(__name__)
  try:
    logger.info("Starting server monitoring at %s", get_local_time())
    monitor_server()
  except KeyboardInterrupt:
    logger.info("Monitoring stopped by user")
    sys.exit(0)
  except Exception as e:
    logger.exception("Monitoring failed: %s", e)
    sys.exit(1)
