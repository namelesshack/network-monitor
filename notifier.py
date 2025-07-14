import smtplib
from email.mime.text import MIMEText

def send_notification(message):
    sender = "your_email@example.com"
    receiver = "admin@example.com"
    password = "your_password"

    msg = MIMEText(message)
    msg['Subject'] = "Server Alert"
    msg['From'] = sender
    msg['To'] = receiver

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
    except Exception as e:
        print(f"Failed to send email: {e}")
