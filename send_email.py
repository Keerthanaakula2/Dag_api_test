import smtplib
from email.mime.text import MIMEText

# Email content
subject = "Test Results"
body = "Test results: Passed"

# Sender and recipient email addresses
sender_email = "techprojectscloud@gmail.com"
recipient_email = "kakula@cswg.com"

# SMTP server details
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Your Gmail account credentials
username = "techprojectscloud@gmail.com"
password = "ziwvonxpxrmghcum"  # App password you generated

# Create MIMEText object
msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = recipient_email

# Connect to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password)

# Send the email
server.sendmail(sender_email, recipient_email, msg.as_string())

# Disconnect from the server
server.quit()