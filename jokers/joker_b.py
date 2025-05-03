#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from .base import Joker

class JokerB(Joker):
    def __init__(self, **kwargs):
        pass

    def get_random_joke(self):
        api_url = "https://icanhazdadjoke.com/slack"
        response = requests.get(api_url)
        result = response.json()
        return f"jokeB: {result['attachments'][0]['text']}"

