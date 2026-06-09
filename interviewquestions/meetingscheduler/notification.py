class Notification:
    def __init__(self, notification_id, message):
        self._notification_id = notification_id
        self._message = message

    def send_meeting_invite_notification(self, user, meeting):
        print("[+] Invite Notification sent to " + user.get_name() + " for meeting: " + meeting.get_subject())

    def send_cancel_meeting_notification(self, user, meeting):
        print("[+] Cancellation Notification sent to " + user.get_name() + " for meeting: " + meeting.get_subject())
