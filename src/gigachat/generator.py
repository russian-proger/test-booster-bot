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

