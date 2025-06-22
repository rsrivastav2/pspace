import win32com.client
import time
from win10toast import ToastNotifier

# Initialize the Windows toast notifier
toaster = ToastNotifier()

# Outlook setup
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # 6 = Inbox
messages = inbox.Items
messages.Sort("[ReceivedTime]", True)

# Store processed message IDs to avoid duplicates
processed_ids = set()

# Define the keyword to search
KEYWORD = "YourKeywordHere"

def show_notification(subject, sender):
    toaster.show_toast(
        "📧 New Matching Email",
        f"From: {sender}\nSubject: {subject}",
        duration=10,  # seconds
        threaded=True
    )

def check_emails():
    for message in messages:
        try:
            entry_id = message.EntryID
            if entry_id in processed_ids:
                continue

            subject = message.Subject
            body = message.Body
            sender = message.SenderName
            received_time = message.ReceivedTime

            if KEYWORD.lower() in subject.lower() or KEYWORD.lower() in body.lower():
                print("✅ New matching email!")
                print(f"From: {sender}")
                print(f"Subject: {subject}")
                print(f"Received: {received_time}")
                show_notification(subject, sender)

            processed_ids.add(entry_id)

        except Exception as e:
            print(f"Error reading email: {e}")

# Main loop - polls inbox every 30 seconds
print("📬 Monitoring Outlook inbox for emails containing:", KEYWORD)
while True:
    check_emails()
    time.sleep(30)
