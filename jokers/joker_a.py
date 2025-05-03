#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from .base import Joker

class JokerA(Joker):
    def __init__(self, **kwargs):
        pass

    def get_random_joke(self):
        api_url = 'https://v2.jokeapi.dev/joke/Misc'
        response = requests.get(api_url)
        result = response.json()

        if result['type'] == 'twopart':
            x = result['setup'] + result['delivery']
        elif result['type'] == 'single':
            x = result['joke']
        return f"jokeA: {x}"

