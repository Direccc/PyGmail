import marimo as mo
from pathlib import Path
from gmail_api import init_gmail_service, send_email

client_file = "client_secret.json"
service = init_gmail_service(client_file)

to_address = 'aaronbalolong49@gmail.com'
email_subject = 'Gmail Crash Course Test Email'
email_body = "This is a test email sent using the Gmail API."
attachment_dir = Path('./attachments')
attachment_files = list(attachment_dir.glob('*'))

response_email_sent = send_email(
    service,
    to_address,
    email_subject,
    email_body,
    body_type='plain',
    attachment_paths=attachment_files
)
print(response_email_sent)