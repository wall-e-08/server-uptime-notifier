import os
from .email import send_email_notification
import logging

logger = logging.getLogger(__name__)

def send_notification(subject, message):
  notifier_type = os.getenv("NOTIFIER_TYPE", "email").lower()

  if notifier_type == "email":
    send_email_notification(subject, message)
  elif notifier_type == "slack":
    raise NotImplementedError("Slack notifier not implemented yet")
  elif notifier_type == "telegram":
    raise NotImplementedError("Telegram notifier not implemented yet")
  else:
    raise ValueError(f"Unknown notifier type: {notifier_type}")