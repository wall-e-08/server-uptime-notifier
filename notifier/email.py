import os
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import logging


logger = logging.getLogger(__name__)

def send_email_notification(subject, message):
  try:
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    email_from = os.getenv("EMAIL_FROM_NAME")
    email_to = os.getenv("EMAIL_TO")
    email_user = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASSWORD")

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = formataddr((email_from, email_user))
    msg['To'] = email_to

    with smtplib.SMTP(smtp_host, smtp_port) as server:
      server.starttls()
      server.login(email_user, email_password)
      server.send_message(msg)

    logger.info("Email notification sent successfully")
  except Exception as e:
    logger.error(f"Failed to send email notification: {str(e)}")
