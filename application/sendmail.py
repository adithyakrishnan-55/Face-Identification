import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_email(subval,msgval,toaddr):
    fromaddr = "" # Add your email id
    
    # instance of MIMEMultipart
    msg = MIMEMultipart()
    
    # storing the senders email address  
    msg['From'] = fromaddr
    
    # storing the receivers email address 
    msg['To'] = ",".join(toaddr)
    
    # storing the subject 
    msg['Subject'] = subval
    
    # string to store the body of the mail
    body = msgval
    
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    

    
    
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    # start TLS for security
    s.starttls()
    
    # Authentication
    s.login(fromaddr, "add app password") # Add your email password
    
    # Converts the Multipart msg into a string
    text = msg.as_string()
    
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
    
    # terminating the session
    s.quit()
    print("Email  send")
