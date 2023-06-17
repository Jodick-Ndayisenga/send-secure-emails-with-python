from email.message import EmailMessage
import smtplib
import ssl
import random

def getCode():
    code = ""
    while (len(code) != 6):
        code = str(random.randint(623451, 723451))
    return code

def SendEmail(email:str) -> str:

    code = getCode()
    emailSender = "njrajajodick@gmail.com"
    password = "ojutjopzyyhtuuez"
    emailReceiver = email

    subject = "Forgot Password"
    body = f"""
    <h1>Forgot Password !! </h1>
    <h1 style="font-size: 20px;">
    Did you request to change your password ?
    </h1>
    <p style="font-size: 20px;">
    If you are not the one, please ignore this message.
    </br></br>
    We try to secure your accounts against malicious activities.
    </br></p>
    <p style="font-size: 25px;">
    This is your verification code:
    <span style="font-weight:600;letter-spacing:2px; font-size:28px;">
    {code}
    </span></p>"""

    my_email = EmailMessage()
    my_email["From"] = emailSender
    my_email["To"] = emailReceiver
    my_email["Subject"] = subject
    my_email.add_alternative(body, subtype='html')  # Specify the body as HTML

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(emailSender, password)
        server.send_message(my_email)

    return code
