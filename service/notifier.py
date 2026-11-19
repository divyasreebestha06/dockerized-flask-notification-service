from service.dispatchers import EmailDispatcher, WebhookDispatcher

class NotificationManager:
    def __init__(self):
        self.channels = {
            "email": EmailDispatcher(),
            "webhook": WebhookDispatcher()
        }

    def dispatch(self, channel: str, recipient: str, content: str):
        dispatcher = self.channels.get(channel.lower())
        if not dispatcher:
            return {"status": "ERROR", "reason": f"Unsupported channel: {channel}"}
        return dispatcher.send(recipient, content)
