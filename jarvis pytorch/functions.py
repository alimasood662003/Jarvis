#email modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#wikipedia  module
import wikipedia

#gmaildict
import gmail_dict

def sendemail(to,subject,content):
    #Setting smtp connection
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465
    smtp_username = 'aliasghar.m@somaiya.edu'
    smtp_password = 'myou xope wkuu lchn'

    #msg container 
    msg = MIMEMultipart()
    msg['From'] = 'aliasghar.m@somaiya.edu'
    msg['To'] = to
    msg['Subject'] = subject
    
    #msg body
    msg.attach(MIMEText(content, 'plain'))

    #establshing smtp connection and sending email
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)       
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to, msg.as_string())
        server.quit()
        print("Email has been sent!")
    except Exception as e:
        print("An error has occuredd whle sending the email.")
        print("Sorry i am not able to send email")

sentence = input("You: ")


def startemail(ogsentence):
    recipient_nickname = ogsentence.split('to')[-1].strip()
    try:
        recipient_email = gmail_dict[recipient_nickname]
    except KeyError:
        print("Pardon me, who should I send the email to?")
        recipient = sentence
        if 'to' in recipient:
            recipient_nickname =  recipient.split('to')[-1].strip()
        else:
            recipient_nickname = recipient

        recipient_email = gmail_dict.get(recipient_nickname)
        if recipient_email is None:
            print("I'm sorry, I couldn't find the email address for that recipient.")        
    print("What is the subject of the email")
    subject = sentence
    print("What  should i write in this email")
    content = sentence
    print("Type or say confirm to send email or say no to not send email")
    confirmation = sentence
    if 'no' not in confirmation:
        sendemail(recipient_email, subject, content)

def searchwikipedia(ogsentence):
    print("searching wikipedia..")
    sentence = sentence.replace("Wikipedia", "")
    results = wikipedia.summary(sentence, sentences = 2)
    print("According to wikipedia..")
    print(f"Jarvis: {results}")
                  