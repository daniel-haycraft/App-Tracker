import datetime
from plyer import notification
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
import time
import subprocess

# Replace <path-to-script> with the actual path to your shell script
import subprocess

# Replace <path-to-script> with the actual path to your shell script
process = subprocess.Popen(['bash', '-c', 'source /Users/danielhaycraft/Desktop/my_program/config.sh && env'], stdout=subprocess.PIPE)
output, error = process.communicate()
if process.returncode != 0:
    raise ValueError(f"Failed to execute ")
env = dict(line.split('=', 1) for line in output.decode().split('\n') if line)


def email(msg):
# Email content
    sender_email = env['RECIPIENT_EMAIL']
    sender_password = env['SENDER_PASSWORD']
    recipient_email = env['RECIPIENT_EMAIL']
    subject = 'Follow Ups'
    body = f'{msg}'
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Add message body
    body_text = MIMEText(body)
    msg.attach(body_text)

    # Connect to SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = sender_email
    smtp_password = sender_password
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.starttls()
    smtp_connection.login(smtp_username, smtp_password)

    # Send email
    smtp_connection.sendmail(sender_email, recipient_email, msg.as_string())

    # Disconnect from SMTP server
    smtp_connection.quit()

def notifi():
    mes = ''
    tdy = datetime.date.today()
    with open('my_file.txt', 'r') as f:
        for lines in f:
            data = [
            line.strip().split(',')
            for line in f
            if line.strip()
        ]
            result = [
            {
                'url': row[0],
                'name': row[1],
                'position': row[2],
                'location': row[3],
                'url_rec': row[4],
                'name_rec': row[5],
                'date': row[6]
            }
            for row in data
            ]
        for res in result:
            date_str = res['date'].strip()
            my_dates = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            time_changes = [datetime.timedelta(days=3), datetime.timedelta(days=6),
            datetime.timedelta(days=9), datetime.timedelta(days=12)]

            for i, time_change in enumerate(time_changes):
                check_date = my_dates + time_change
                if check_date == tdy:
                    mes +=  f" \n COMPANY: {res['name']}, \n REC URL:{res['url_rec']}, \n NAME REC: {res['name_rec']}, \n APPLICATION URL: {res['url']},\n POSITION: {res['position']} \n {res['date']}\n "
        if mes:
            email(mes)
            notification.notify(title='Linkedin', 
            message='Check Email for Linkedin Reminders!!!',
            app_name="My Apps",
            )



notifi()