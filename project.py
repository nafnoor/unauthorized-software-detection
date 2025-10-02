cmd = "reg query HKEY_CURRENT_USER\SOFTWARE\ > software_list.txt"
myBat = open(r"F:\project\ab.bat", 'w+')
myBat.write(cmd)
myBat.close()

import subprocess
subprocess.call([r"F:\project\ab.bat"])

#read = open(r'D:\Cyber_security\Python\software_list.txt', 'r')
with open(r"F:\project\software_list.txt", 'r') as file:
    read = file.read()
lines = read.split("\n")
wrt = open(r"F:\project\soft_list.txt", 'w')
for line in lines:
    wrt.write(line.split("\\")[-1] + "\n")
wrt.close()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

send_from = "ij6226934@gmail.com"
send_to = "ijahan736@gmail.com"


msg = MIMEMultipart()
msg['From'] = send_from
msg['To'] = send_to
msg['Subject'] = "Assignment"

#filename = "soft_list.txt"
#attachment = open(r"C:\Users\USER\Cyber_security\Python\soft_list.txt", "rb")
#p = MIMEBase('application', 'octet-stream')
#p.set_payload((attachment).read())
#encoders.encode_base64(p)
#p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#msg.attach(p)
#s = smtplib.SMTP('smtp.gmail.com', 587)
#s.starttls()
#s.login(send_from, "password")
#text = msg.as_string()
#s.sendmail(send_from, send_to, text)
#s.quit()
#attachment.close()


import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(r"F:\project\client_secret.json",scope)
client = gspread.authorize(creds)

sheet = client.open("soft_list").sheet1   
 
col = sheet.col_values(1)
pp(col)

with open(r"F:\project\soft_list.txt", "r") as file:
    so = file.read()
    sf = so.split("\n")

    eliminated = []
    for x in sf:
        if x not in col:
            #print(x)
            eliminated.append(x)
            eliminated = [i for i in eliminated if i]
        else:
            pass
                
print("Eliminated\n")
print(eliminated)

spreadsheetId = '1dx1mMZ1KcaPI7xviTJryH3FMpxaH16ioH-qDMoFoqYw'
sheetName = 'sheet1'
sheet.update("D2", [[e] for e in eliminated], value_input_option="USER_ENTERED")
