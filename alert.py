import datetime
from plyer import notification
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
def email(msg):
# Email content
    sender_email = 'dhcopy1@gmail.com'
    sender_password = os.environ['SENDER_PASSWORD']
    recipient_email = 'dhcopy1@gmail.com'
    subject = 'Messages'
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
        time_change = datetime.timedelta(days=3)
        check_time = my_dates + time_change
        if check_time == tdy:
            mes +=  f" \n COMPANY: {res['name']}, \n REC URL:{res['url_rec']}, \n NAME REC: {res['name_rec']}, \n APPLICATION URL: {res['url']},\n POSITION: {res['position']} \n "
    if mes:
        email(mes)
        notification.notify(title='Linkedin', 
        message='check Email for linkedin Reminders!!!',
        app_name="My Apps")
    else:
        print('no one')
            

