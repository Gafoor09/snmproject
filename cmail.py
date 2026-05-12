import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('gafoorsk474@gmail.com','zcrj yznd dixh nima')
    msg=EmailMessage()
    msg['FROM']='gafoorsk474@gmail.com'
    msg['SUBJECT']=subject
    msg['TO']=to
    msg.set_content(body)
    server.send_message(msg)
    server.close()
