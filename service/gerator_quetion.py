import groq

import os

system_prompt = ""


class chat:
    def __init__(self):
        self.key = os.getenv("groq_api")
        self.system_prompt = system_prompt
        self.client = groq.Groq(api_key=self.key)

    def format_system_prompt(self, dificuldade: str, max_question: int) -> str:
        return f"""
        Você é um professor que irá gerar max_question questões no formato JSON.
        Exemplo:
        {{
        "enunciado": "texto da questão",
        "resposta1": {{ "texto": "opção A", "correta": false }},
        "resposta2": {{ "texto": "opção B", "correta": true }},
        "resposta3": {{ "texto": "opção C", "correta": false }},
        "resposta4": {{ "texto": "opção D", "correta": false }}
        }},
        
        apenas gere o json

        Config:
        max_question: {max_question}
        dificuldade: {dificuldade}
        não adiconar: ```json ```
        """

    def geration_quetion(self, Contexto: str, text: str) -> str:
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": Contexto
                },
                {
                    "role": "user",
                    "content": text,
                }
            ], 
            model="openai/gpt-oss-120b")
        return chat_completion.choices[0].message.content
        