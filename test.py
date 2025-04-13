import importlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

scripts = ['script1', 'script2', 'script3']  # Add all script filenames without `.py`

results = []

for script in scripts:
    try:
        module = importlib.import_module(script)
        module.run()  # assuming each script has a run() function
        results.append((script, 'PASS'))
    except Exception as e:
        results.append((script, f'FAIL: {str(e)}'))

# Generate HTML table
html = """
<html>
<head></head>
<body>
<p>Test Report:</p>
<table border="1" cellpadding="5" cellspacing="0">
<tr><th>Script</th><th>Status</th></tr>
"""

for script, status in results:
    color = "green" if "PASS" in status else "red"
    html += f"<tr><td>{script}</td><td style='color:{color};'><b>{status}</b></td></tr>"

html += """
</table>
</body>
</html>
"""

# Email config
sender = "your_email@example.com"
receiver = "recipient@example.com"
subject = "Selenium Test Report"

msg = MIMEMultipart("alternative")
msg["Subject"] = subject
msg["From"] = sender
msg["To"] = receiver

msg.attach(MIMEText(html, "html"))

# Send the email
with smtplib.SMTP("smtp.example.com", 587) as server:
    server.starttls()
    server.login("your_email@example.com", "your_password")
    server.sendmail(sender, receiver, msg.as_string())
