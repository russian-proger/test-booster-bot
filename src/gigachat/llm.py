""" GigaChat LLM """

import os
from langchain_gigachat.chat_models import GigaChat
from ..utils.singleton import singleton

@singleton
def get_llm() -> GigaChat:
    """ Create instance of GigaChat """
    return GigaChat(
        credentials=os.environ['GIGACHAT_AUTH_KEY'],
        scope=os.environ['GIGACHAT_SCOPE'],
        model='GigaChat',
        verify_ssl_certs=False,
        streaming=False,
    )
