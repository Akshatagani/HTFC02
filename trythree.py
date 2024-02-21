import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['To'] = to

    user = "akshatagani67@gmail.com"
    msg['From'] = user
    password = "dfkxuwfecbkrjzef"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

if __name__ == '__main__':
    email_alert("ALERT!", "Someone is trying to make a transaction from your account. Is this you??", "Sujithak7854@gmail.com")
