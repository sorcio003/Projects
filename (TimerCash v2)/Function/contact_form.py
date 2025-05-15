import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from .pdf_crate import create_invoice

def pdf(receiver, pay, time, start_time, end_time, total):
    invoice_number = ""
    with open('Database/fatture_id.txt', "r") as fatture:
        invoice_number = fatture.readline().strip()
        invoice_number = int(invoice_number) + 1
        print(invoice_number) 
        
    with open('Database/fatture_id.txt', "w") as fatture:
        fatture.write(str(invoice_number))
        
    invoice_data = {
        'invoice_number': 'INV00' + str(invoice_number),
        'invoice_date': time.strftime("%d/%m/%Y"),
        'provider_name': receiver[0] + " " + receiver[1],
        'items': [
            {'description': 'Servizio di ' + receiver[5], 
             'quantity': 1, 
             'hourly_rate': str(receiver[4]) + " €",
             'total': str(pay) +" €" ,
             'start_time': start_time, 
             'end_time': end_time, 
             'total_hours': total }
        ],
        'total_amount': pay
        }

    create_invoice("fattura.pdf", invoice_data, receiver, time)

def SendEmail(finished, receiver, pay):
    password = "vfou jlwf kvxx uaal"
    
    email = "pythontimercash@gmail.com"
    
    time = datetime.now()
    
    pay = round(pay, 2)
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "Python Timer Cash Auto Message"
    message["From"] = email
    message["To"] = receiver[2]

    text = """"""
    
    html = """"""
    
    if not finished:
        html = """\
        <html>
        <body>
    <p style="font-size:xx-large;" align="center"> <strong>Il tuo lavoro <br> è appena <br> Iniziato</strong></p>
    <div align="center">
        <img src="cid:Mailtrapimage" alt="logo" style="width: 300px;">
    </div>
    <div align="center">
        <div style="background-color: rgba(157, 215, 211, 0.255); width:75%; text-align:left; padding: 2%; " >
            <p>Ciao, """ + receiver[0] + """</p>
            <p>Siamo orgogliosi di comunicarti che il tuo lavoro è iniziato alle ore """ + time.strftime("%X") + """.</p>
            <p>Vogliamo ricordati che il tuo lavoro richiede """ + receiver[4] + """ € ad ora.</p>
            <p>Se i dettagli riportati sopra non corrispondono con i termini sottoscritti con il tuo cliente o datore di lavoro
                ti preghiamo di fermare il timer dall'app e riavviare il timer con i dati corretti inseriti.
            </p>
            <p>Ti ricordiamo che al fine di rendere questa applicazione attendibile per il tuo lavoro, la stessa e-mail verrà
                inviata al tuo cliente o datore di lavoro per non incorrere in incomprensione sull'aspetto monetario
                (salario). <br>
                E che alla fine del conteggio ore, in allegato alla e-mail verrà messo un file di fattura con riportati: <br><br>
                - Le ore lavorate
                <br>
                - Il tipo di lavoro svolto
                <br>
                - Info recapito lavoratore 
                <br>
                - Date e ora 
            </p>
        </div>
        <p>Python Timer Cash</p>
    </div> 
        </body>
        </html>
        """
    else:    
        html = """
            <html>
            <body>
            <p style="font-size:xx-large;" align="center"> <strong>Il tuo lavoro <br> è appena <br> Finito </strong></p>
            <div align="center">
                <img src="cid:Mailtrapimage" alt="logo" style="width: 300px;">
            </div>
            <div align="center">
            <div style="background-color: rgba(157, 215, 211, 0.255); width:75%; text-align:left; padding: 2%; " >
            <p>Ciao, """ + receiver[0] + """</p>
            <p>Siamo orgogliosi di comunicarti che il tuo lavoro è finito alle ore """ + time.strftime("%X") + """.</p>
            <p>Vogliamo ricordati che il tuo lavoro richiede """ + str(pay) + """ € totali.</p>
            <p>Se i dettagli riportati sopra non corrispondono con i termini sottoscritti con il tuo cliente o datore di lavoro
                ti preghiamo di controllare la mail secondaria mandata al tuo cliente o datore di lavoro, o ricontare manualmente il totale manualmente
                se i dati inseriti a inizio lavoro erano scorretti.
            </p>
            <p>Ti ricordiamo che al fine di rendere questa applicazione attendibile per il tuo lavoro, la stessa e-mail verrà
                inviata al tuo cliente o datore di lavoro per non incorrere in incomprensione sull'aspetto monetario
                (salario). <br>
                E che alla fine del conteggio ore, in allegato alla e-mail verrà messo un file di fattura con riportati: <br><br>
                - Le ore lavorate
                <br>
                - Il tipo di lavoro svolto
                <br>
                - Info recapito lavoratore 
                <br>
                - Date e ora 
            </p>
        </div>
        <p>Python Timer Cash</p>
    </div> 
        </body>
        </html>
        """
        with open('fattura.pdf', "rb") as attachment:
            part = MIMEApplication(attachment.read(), _subtype="pdf")
            part.add_header('Content-Disposition', 'attachment', filename='fattura.pdf')
            message.attach(part)
    
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    fp = open('Assets/logo.png', 'rb')
    image = MIMEImage(fp.read())
    fp.close()

    image.add_header('Content-ID', '<Mailtrapimage>')
    message.attach(image)

    sever = smtplib.SMTP("smtp.gmail.com:587")
    sever.starttls()
    sever.login(email, password)
    sever.sendmail(email, receiver[2], message.as_string())
    sever.quit()

    print("Email has been sent to " + receiver[2])

def SendEmailCliente(finished, receiver, pay):
        
    password = "vfou jlwf kvxx uaal"
    
    email = "pythontimercash@gmail.com"
    
    time = datetime.now()
    
    pay = round(pay, 2)
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "Python Timer Cash Auto Message"
    message["From"] = email
    message["To"] = receiver[3]

    text = """"""
    
    html = """"""
    
    if not finished:        
        html = """\
        <html>
        <body>
    <p style="font-size:xx-large;" align="center"> <strong>Il tuo lavoro <br> è appena <br> Iniziato</strong></p>
    <div align="center">
        <img src="cid:Mailtrapimage" alt="logo" style="width: 300px;">
    </div>
    <div align="center">
        <div style="background-color: rgba(157, 215, 211, 0.255); width:75%; text-align:left; padding: 2%; " >
            <p>Gentile Cliente,</p>
            <p>Siamo orgogliosi di comunicarti che il lavoro da te richiesto a """ + receiver[0] + """ """ + receiver[1] + """ è iniziato alle ore """ + time.strftime("%X") + """.</p>
            <p>Vogliamo ricordati che il lavoro richiede """ + receiver[4] + """ € ad ora.</p>
            <p>Se i dettagli riportati sopra non corrispondono con i termini sottoscritti con il tuo cliente o datore di lavoro
                ti preghiamo di fermare il timer dall'app e riavviare il timer con i dati corretti inseriti.
            </p>
            <p>Ti ricordiamo che al fine di rendere questa applicazione attendibile per il tuo lavoro, la stessa e-mail verrà
                inviata al tuo cliente o datore di lavoro per non incorrere in incomprensione sull'aspetto monetario
                (salario). <br>
                E che alla fine del conteggio ore, in allegato alla e-mail verrà messo un file di fattura con riportati: <br><br>
                - Le ore lavorate
                <br>
                - Il tipo di lavoro svolto
                <br>
                - Info recapito lavoratore 
                <br>
                - Date e ora 
            </p>
        </div>
        <p>Python Timer Cash</p>
    </div> 
        </body>
        </html>
        """
    else:            
        html = """\
        <html>
        <body>
<p style="font-size:xx-large;" align="center"> <strong>Il tuo lavoro <br> è appena <br> Finito </strong></p>
    <div align="center">
        <img src="cid:Mailtrapimage" alt="logo" style="width: 300px;">
    </div>
    <div align="center">
        <div style="background-color: rgba(157, 215, 211, 0.255); width:75%; text-align:left; padding: 2%; " >
            <p>Gentile Cliente,</p>
            <p>Siamo orgogliosi di comunicarti che il lavoro da te richiesto a """ + receiver[0] + """ """ + receiver[1] + """ è finito alle ore """ + time.strftime("%X") + """.</p>
            <p>Vogliamo ricordati che il lavoro richiede """ + str(pay) + """ € totali.</p>
            <p>Se i dettagli riportati sopra non corrispondono con i termini sottoscritti con il tuo cliente o datore di lavoro
                ti preghiamo di controllare la mail secondaria mandata al tuo cliente o datore di lavoro, o ricontare manualmente il totale manualmente
                se i dati inseriti a inizio lavoro erano scorretti.
            </p>
            <p>Ti ricordiamo che al fine di rendere questa applicazione attendibile per il tuo lavoro, la stessa e-mail verrà
                inviata al tuo cliente o datore di lavoro per non incorrere in incomprensione sull'aspetto monetario
                (salario). <br>
                E che alla fine del conteggio ore, in allegato alla e-mail verrà messo un file di fattura con riportati: <br><br>
                - Le ore lavorate
                <br>
                - Il tipo di lavoro svolto
                <br>
                - Info recapito lavoratore 
                <br>
                - Date e ora 
            </p>
        </div>
        <p>Python Timer Cash</p>
    </div> 
        </body>
        </html>
        """
        with open('fattura.pdf', "rb") as attachment:
            part = MIMEApplication(attachment.read(), _subtype="pdf")
            part.add_header('Content-Disposition', 'attachment', filename='fattura.pdf')
            message.attach(part)
    
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    fp = open('Assets/logo.png', 'rb')
    image = MIMEImage(fp.read())
    fp.close()

    image.add_header('Content-ID', '<Mailtrapimage>')
    message.attach(image)

    sever = smtplib.SMTP("smtp.gmail.com:587")
    sever.starttls()
    sever.login(email, password)
    sever.sendmail(email, receiver[3], message.as_string())
    sever.quit()

    print("Email has been sent to " + receiver[3])
