import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('notifications', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('notifications', self.channel_name)

    async def receive(self, text_data):
        # For demo: echo back or ignore
        pass

    async def send_notification(self, event):
        await self.send(text_data=json.dumps({
            'type': event.get('type', 'notification'),
            'message': event['message'],
            'title': event.get('title', 'Notification'),
        })) 