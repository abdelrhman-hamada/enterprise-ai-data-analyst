from pydantic import BaseModel
from typing import List


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatStartResponse(BaseModel):
    session_id: str


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str


class ChatHistoryResponse(BaseModel):
    messages: List[ChatMessage]