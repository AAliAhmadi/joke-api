#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from abc import ABC, abstractmethod

class Joker(ABC):
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def get_random_joke(self):
        pass

