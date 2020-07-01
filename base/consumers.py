from datetime import datetime, date
from channels.db import database_sync_to_async as db_async_conn
from channels.generic.websocket import AsyncWebsocketConsumer

class ModAsyncWebsocketConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @db_async_conn
    def asyncify(self, asyncable, **kwargs):
        return asyncable
