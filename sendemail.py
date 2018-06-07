from email.mime.text import MIMEText
import smtplib

def sendemail():
    FROM = 'Silver@uci.edu'
    SENTTo = 'amyelsayed@gmail.com'
    SUBJECT = "Hello!"
    TEXT = "This message was sent by Silver"
    msg = MIMEText('body')
    msg['Subject'] = 'subject'
    msg['From'] = "..."
    msg['Reply-to'] = "..."
    msg['To'] = "..."
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.ehlo()
    mail.login("affinemirror", "howareyouiman")
    # mail.login('kufeilin@gmail.com','kufeilin2017')
    mail.sendmail('affinemirror@gmail.com', SENTTo, TEXT)
    print("Sent Succesffuly")
    mail.close()


if __name__ == "__main__":
    sendemail()