import logging


def init_configure_logging(enable=True):
  if not enable:
    return
  logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)-10s: %(name)-20s -> %(message)s',
    handlers=[
      logging.StreamHandler(),
      logging.FileHandler('notifications.log')
    ]
  )
