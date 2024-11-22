import asyncio
from typing import Dict, Type, Any
from pydantic import BaseModel

class Request(BaseModel):
    pass

class Response(BaseModel):
    pass

class Mediator:
    def __init__(self):
        self.handlers: Dict[Type[Request], Any] = {}

    def register(self, request_type: Type[Request], handler):
        self.handlers[request_type] = handler

    async def send(self, request: Request) -> Response:
        handler = self.handlers.get(type(request))
        if not handler:
            raise Exception(f"No handler registered for {type(request).__name__}")
#        if asyncio.iscoroutinefunction(handler):
#            return await handler(request)
        return await handler(request)