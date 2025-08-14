import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()
sender_email = os.getenv("EMAIL_ADDRESS")
sender_password = os.getenv("EMAIL_PASSWORD")

def send_email(to_email, message):
    try:
        msg = MIMEText(message)
        msg['Subject'] = "Cube AI Greetings"
        msg['From'] = sender_email
        msg['To'] = to_email

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        return True

    except smtplib.SMTPAuthenticationError as e:
        print("❌ SMTP Authentication failed:", e)
        return False

    except Exception as e:
        print("❌ General error:", e)
        return False
