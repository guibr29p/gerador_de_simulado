import groq

import os

system_prompt = ""


class chat:
    def __init__(self):
        self.key = os.getenv("groq_api")
        self.system_prompt = system_prompt
        self.client = groq.Groq(api_key=self.key)


        