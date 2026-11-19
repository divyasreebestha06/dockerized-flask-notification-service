import unittest
from service.notifier import NotificationManager

class TestNotificationService(unittest.TestCase):
    def setUp(self):
        self.mgr = NotificationManager()

    def test_email_dispatch(self):
        res = self.mgr.dispatch("email", "divyasreebestha161@gmail.com", "Your interview is scheduled!")
        self.assertEqual(res["status"], "DELIVERED")
        self.assertEqual(res["channel"], "EMAIL")

    def test_webhook_dispatch(self):
        res = self.mgr.dispatch("webhook", "https://api.example.com/hooks", "Order completed")
        self.assertEqual(res["status"], "DELIVERED")
        self.assertEqual(res["channel"], "WEBHOOK")

    def test_invalid_channel(self):
        res = self.mgr.dispatch("pigeon", "rooftop", "msg")
        self.assertEqual(res["status"], "ERROR")

if __name__ == "__main__":
    unittest.main()
