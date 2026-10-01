import os
import uuid
import requests


OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2"
)


chat_sessions = {}


def create_session(context: str):

    session_id = str(uuid.uuid4())

    chat_sessions[session_id] = {
        "context": context,
        "messages": []
    }

    return session_id


def get_session(session_id: str):

    session = chat_sessions.get(session_id)

    if session is None:
        raise ValueError("Chat session not found")

    return session


def ask_ollama(
    session_id: str,
    question: str
):

    session = get_session(session_id)

    system_message = f"""
You are an expert data analyst.

You are analyzing a dataset using the dataset report below.

Rules:
- Answer only using information available in the dataset report.
- Never invent statistics or values.
- If the report does not contain enough information, say so.
- Explain findings clearly.
- Remember the previous conversation.
- When the user asks a follow-up question, use the conversation history.

Dataset Report:
{session["context"]}
"""

    messages = [
        {
            "role": "system",
            "content": system_message
        }
    ]

    messages.extend(session["messages"])

    messages.append({
        "role": "user",
        "content": question
    })

    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/chat",
        json={
            "model": OLLAMA_MODEL,
            "messages": messages,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    answer = data["message"]["content"]

    session["messages"].append({
        "role": "user",
        "content": question
    })

    session["messages"].append({
        "role": "assistant",
        "content": answer
    })

    return answer


def get_chat_history(session_id: str):

    session = get_session(session_id)

    return session["messages"]