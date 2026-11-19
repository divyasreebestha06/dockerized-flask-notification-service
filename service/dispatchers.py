from typing import Dict, Any

class BaseDispatcher:
    def send(self, recipient: str, message: str) -> Dict[str, Any]:
        raise NotImplementedError

class EmailDispatcher(BaseDispatcher):
    def send(self, recipient: str, message: str) -> Dict[str, Any]:
        if "@" not in recipient:
            return {"status": "FAILED", "reason": "Invalid email"}
        return {"status": "DELIVERED", "channel": "EMAIL", "recipient": recipient, "preview": message[:30]}

class WebhookDispatcher(BaseDispatcher):
    def send(self, recipient: str, message: str) -> Dict[str, Any]:
        if not recipient.startswith("http"):
            return {"status": "FAILED", "reason": "Invalid URL"}
        return {"status": "DELIVERED", "channel": "WEBHOOK", "target_url": recipient}
