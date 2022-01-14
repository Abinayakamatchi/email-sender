import smtplib 
from email.message import EmailMessage
from string import Template 
from pathlib import Path 
html=Template(Path('index.html').read_text())
email=EmailMessage() 
email['from']= 'abinaya kamatchi s'
email['to']='abinayaakamatchi@gmail.com'
email['subject']='you won 1,000,000 dollars!' 
email.set_content(html.substitute({'name':'abinaya'}),'html')

with smtplib.SMTP(host= "smtp.gmail.com",port= 587) as smtp:
	smtp.ehlo()
	smtp.starttls() 
	smtp.login('abhinaya662@gmail.com','lingabairavi662')
	smtp.send_message(email)