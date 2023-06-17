# Send emails with python

This is a Python script that defines a function called SendEmail. This function is used to send an email containing a verification code to a specified email address. Here's a step-by-step explanation of the code:

````python
from email.message import EmailMessage
import smtplib
import ssl
import random
````
The code begins by importing the necessary modules: EmailMessage from the email.message module, smtplib for sending emails, ssl for creating a secure connection, and random for generating a random verification code.

````python

def getCode():
    code = ""
    while (len(code) != 6):
        code = str(random.randint(623451, 723451))
    return code
````
The getCode function generates a random 6-digit code. It uses a while loop to generate random numbers until a 6-digit code is obtained. The code is converted to a string and returned.

````python

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
````
The SendEmail function takes an email address as a parameter and returns the generated verification code. Inside the function, the getCode function is called to generate the verification code. The email sender's address, password, and the recipient's email address are assigned to variables (emailSender, password, and emailReceiver, respectively).

The subject of the email is set as "Forgot Password". The body of the email is defined as an HTML string, containing various HTML tags and placeholders where the code will be inserted.

````python

    my_email = EmailMessage()
    my_email["From"] = emailSender
    my_email["To"] = emailReceiver
    my_email["Subject"] = subject
    my_email.add_alternative(body, subtype='html')
````
An instance of EmailMessage is created and configured. The sender, recipient, and subject are set using the respective properties of the my_email object. The add_alternative method is used to attach the HTML body to the email, specifying the subtype as 'html'.

````python

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(emailSender, password)
        server.send_message(my_email)
````
A secure SSL context is created using ssl.create_default_context(). This context is used to establish a secure connection with the Gmail SMTP server.

A connection is established with the SMTP server using smtplib.SMTP_SSL. The server address is specified as "smtp.gmail.com" and the port as 465. The login method is called to authenticate with the sender's email address and password.

Finally, the email message (my_email) is sent using the send_message method of the server object.

````python

    return code
````
The verification code is returned from the SendEmail function.

Overall, this code allows you to send an email containing a verification code to a specified email address using Gmail's SMTP server. It generates a random code, constructs an HTML email with the code, and sends it securely to the recipient.