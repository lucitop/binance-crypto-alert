def send_notification(pb, title, message):
    try:
        pb.push_note(title, message)
        print(f"Notification sent: {title} - {message}")
    except Exception as e:
        print(f"Failed to send notification: {e}")
