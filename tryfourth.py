import smtplib
import csv
from email.message import EmailMessage

def read_email_addresses(file_path):
    emails = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            emails.extend(row)
    return emails

def email_alert(subject, body, recipients):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = "akshatagani67@gmail.com"
    msg['To'] = ", ".join(recipients)

    password = "dfkxuwfecbkrjzef"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(msg['From'], password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    # Provide the path to the dataset containing email addresses
    dataset_path = "C:\\Users\\Akshata\\Desktop\\email.csv"
    recipients = read_email_addresses(dataset_path)
    email_alert("ALERT!", "Someone is trying to make a transaction from your account. Is this you??", recipients)
