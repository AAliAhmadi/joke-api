#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from jokers.joker_a import JokerA
from jokers.joker_b import JokerB
from jokers.joker_c import JokerC

if __name__ == '__main__':
    jokeA = JokerA()
    print(jokeA.get_random_joke())

    jokeB = JokerB()
    print(jokeB.get_random_joke())

    API = ''
    jokeC = JokerC(api_token=API)
    try:
        print(jokeC.get_random_joke())
    except:
        print("""If you want a third joke from api.api-ninjas.com, you need a valid API key.
Visit https://api.api-ninjas.com and get a valid API key, then paste it in the API variable.""")


