# smtp allows us to use a server protocol to send the message
# simple mail transfer protocol
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # simliar to os.path


html = Template(Path('index.html').read_text())

email = EmailMessage()
email['subject'] = f'Python Messaged You!'
email['from'] = 'Monsta'
email['to'] = 'david_escobar-13@hotmail.com'


email.set_content(html.substitute(name = 'George'), 'html')

email_addr = 'monstacrafter@gmail.com'
email_pssw = 'jxotxnfarhpjtjut'

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
	# creates sever
	smtp.ehlo()
	# encrypts
	smtp.starttls()
	# login
	smtp.login(email_addr, email_pssw)
	smtp.send_message(email)

	print('sent!')