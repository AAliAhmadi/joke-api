#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from .base import Joker

class JokerC(Joker):
    def __init__(self, **kwargs):
        self.api_key = kwargs.get('api_token')

    def get_random_joke(self):
        api_url = 'https://api.api-ninjas.com/v1/jokes?limit=1'
        response = requests.get(api_url, headers={'X-Api-Key': self.api_key})
        result = response.json()
        return f"jokeC: {result[0]['joke']}"

