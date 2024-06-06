import smtplib, ssl

host = "smtp.gmail.com"
port = 465


username= "joeskokan20@gmail.com"
password = "awmqjgjfyymrelfr"

receiver = "joeskokan20@gmail.com"
context = ssl.create_default_context()

message = '''\
Subject: Testing apps!
How are you?
see YA!
'''
with smtplib.SMTP_SSL(host, port, context =context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)






# awmq jgjf yymr elfr