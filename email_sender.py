import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'May Salcedo'
email['to'] = 'mayann18na@yahoo.com'
email['subject'] = 'Wow you look great today!'
email.set_content(html.substitute({'name':'Tintin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('python.enthusiast2020@gmail.com', 'M3rc@d01')
    smtp.send_message(email)
    print('all good madam')
