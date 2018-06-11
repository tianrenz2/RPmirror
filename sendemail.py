from email.mime.text import MIMEText
import smtplib

def sendemail():
    FROM = 'fromemail'
##    SENTTo = 'email@gmail.com'
    SENTTo = 'toemail@gmail.com'
    SUBJECT = "Alarm"
    TEXT = "INTRUDER INTRUDER!"
    msg = MIMEText('body')
    msg['Subject'] = 'subject'
    msg['From'] = "..."
    msg['Reply-to'] = "..."
    msg['To'] = "..."
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.ehlo()
    mail.login("email", "password")
    mail.sendmail('affinemirror@gmail.com', SENTTo, TEXT)
    print("Sent Succesffuly")
    mail.close()
