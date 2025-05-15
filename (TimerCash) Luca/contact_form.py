import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def SendEmail(finished, receiver, pay):
    password = "vfou jlwf kvxx uaal"
    
    email = "pythontimercash@gmail.com"
    
    time = datetime.now()
    
    pay = round(pay, 2)
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "Python Timer Cash Auto Message"
    message["From"] = email
    message["To"] = receiver[2]

    """
    subject = "Python Script TimerCash"
    Message = ""
    if not finished:
        Message = "Your worker " + receiver[0] + " " + receiver[1] + " has started its own work at " + time.strftime("%X")
    else:
        Message = "Your worker " + receiver[0] + " " + receiver[1] + " has finished its own work at " + time.strftime("%X") + "\nYour worker have to be payed! You must pay " + str(pay) + " Euro"
    text = f"Subject: {subject}\n\n{Message}"

    """

    text = """"""
    
    html = """"""
    
    if not finished:
        html = """\
        <html>
        <body>
            <p>Goodmorning,<br>
            Your own worker """ + receiver[0] + """ """ + receiver[1] + """ has started is own work at """ + time.strftime("%X") + """</p>
            <p>Please, if this email doesn't match with daily work time, contact you worker <br> at dependent email: """ + receiver[2] + """</p>  
        </body>
        </html>
        """
    else:
        html = """\
        <html>
        <body>
            <p>Goodmorning,<br>
            Your own worker """ + receiver[0] + """ """ + receiver[1] + """ has finished is own work at """ + time.strftime("%X") + """</p>
            <p>You have to pay """ + str(pay) + """ € at your worker</p>
            <p>Please, if this email doesn't match with daily work time, contact you worker <br> at dependent email: """ + receiver[2] + """</p> 
        </body>
        </html>
        """
    
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    sever = smtplib.SMTP("smtp.gmail.com", 587)
    sever.starttls()

    sever.login(email, password)
    sever.sendmail(email, receiver, message.as_string())

    print("Email has been sent to " + receiver[2])
