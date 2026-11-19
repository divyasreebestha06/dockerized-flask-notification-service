from service.notifier import NotificationManager

manager = NotificationManager()

def api_send_notification(payload: dict):
    channel = payload.get("channel")
    recipient = payload.get("recipient")
    content = payload.get("message")
    if not all([channel, recipient, content]):
        return {"error": "Missing parameters"}, 400
    res = manager.dispatch(channel, recipient, content)
    return res, 200
