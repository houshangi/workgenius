from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class OpenEvent(BaseModel):
    ts: datetime


class ClickEvent(BaseModel):
    ts: datetime
    url: str


class Metadata(BaseModel):
    user_id: int


class Message(BaseModel):
    ts: datetime
    subject: str
    email: str
    sender: str
    tags: List[str]
    opens: Optional[List[OpenEvent]]
    clicks: Optional[List[ClickEvent]]
    state: str
    metadata: Optional[Metadata]
    id: str
    _version: str

    class Config:
        fields = {'id': '_id'}


class MandrillEvent(BaseModel):
    event: str
    msg: Message


class MandrillEvents(BaseModel):
    mandrill_events: List[MandrillEvent]

