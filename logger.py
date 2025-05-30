import logging


def init_configure_logging(enable=True):
  if not enable:
    return
  logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-10s: %(message)s',
    handlers=[
      logging.StreamHandler(),
      logging.FileHandler('notifications.log')
    ]
  )
