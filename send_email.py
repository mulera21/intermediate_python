import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "edmondmulera55@gmail.com"
password = "hakx yojl vstq fwyr"

receiver = "edmondmulera55@gmail.com"
context = ssl.create_default_context()

message = """\
subject: hi Ed 
how are you
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
