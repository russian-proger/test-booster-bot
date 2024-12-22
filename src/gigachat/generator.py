""" Message generator """

from langchain_core.messages import HumanMessage, SystemMessage
from .llm import get_llm

def generate_start_message():
    """ Generate greeting message """
    messages = [
        SystemMessage(
            content="Ты телеграм бот для проведения онлайн тестирования"),
        HumanMessage(content="Привет! Кто ты и чем ты мне можешь помочь?")
    ]
    res = get_llm().invoke(messages)
    return res.content

def generate_message(system_prompt: str|None, user_prompt: str|None):
    """ Generate custom message """
    messages: list[SystemMessage|HumanMessage] = []

    if system_prompt:
        messages.append(SystemMessage(content=system_prompt))

    if user_prompt:
        messages.append(HumanMessage(content=user_prompt))

    res = get_llm().invoke(messages)
    return res.content
