# set_up_alerts.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from whylogs import DatasetProfile, get_or_create_session

def send_alert(email_recipient, email_subject, email_body):
    email_sender = "your_email@example.com"
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_recipient
    msg['Subject'] = email_subject

    msg.attach(MIMEText(email_body, 'plain'))

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(email_sender, "your_password")
        text = msg.as_string()
        server.sendmail(email_sender, email_recipient, text)

def check_model_performance():
    session = get_or_create_session()
    profiles = session.list()
    
    for profile in profiles:
        if profile.name == "model_performance":
            if profile.metrics["rmse"].last > 0.1:
                send_alert(
                    email_recipient="alert_recipient@example.com",
                    email_subject="Model Performance Alert",
                    email_body=f"RMSE threshold exceeded: {profile.metrics['rmse'].last}"
                )
                break

if __name__ == "__main__":
    check_model_performance()
