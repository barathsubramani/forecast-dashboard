import smtplib, ssl


def send_emails(message):
    host = "smtp.gmail.com"
    port = 465
    username = "barathsubramani77@gmail.com"
    password = "vsigxavkkzqvknmx"
    receiver = "barathsubramani77@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

