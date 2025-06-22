import win32com.client
import time

# Set up Outlook connection
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

# Access Inbox
inbox = outlook.GetDefaultFolder(6)  # 6 = Inbox
messages = inbox.Items
messages.Sort("[ReceivedTime]", True)  # Sort by most recent

# Keep track of already seen messages
processed_ids = set()

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

            # Add your condition here
            if "YourKeywordHere" in subject or "YourKeywordHere" in body:
                print("New matching email received!")
                print(f"From: {sender}")
                print(f"Subject: {subject}")
                print(f"Received: {received_time}")
                # Add logic to store or act on it here
                # For example: save to DB, trigger API call, etc.

            processed_ids.add(entry_id)
        except Exception as e:
            print(f"Error: {e}")

# Poll every 30 seconds
while True:
    check_emails()
    time.sleep(30)
