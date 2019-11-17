import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

API_KEY = os.environ("API_KEY")

def send_email(content):
    message = Mail(
        from_email='from_email@example.com',
        to_emails='gtalarico@gmail.com',
        subject='AU 2019 - BIM forever',
        html_content=content
    )

    try:
        sg = SendGridAPIClient(API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
