from modules.alerts import send_email

send_email(
    "SentinelOps Test",
    "This is a test email from SentinelOps."
)

print("Email sent successfully.")
