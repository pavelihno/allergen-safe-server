import os, json

from jinja2 import Environment, FileSystemLoader
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

model = 'open-mixtral-8x22b'
# model = 'mistral-large-latest'

client = MistralClient(api_key=os.environ.get('AI_API_KEY'))

def __get_ai_response(message):
    messages = [ChatMessage(role='user', content=message)]
    chat_response = client.chat(
        model=model,
        response_format={'type': 'json_object'},
        messages=messages,
    )
    response = chat_response.choices[0].message.content
    return json.loads(response)

def get_ai_response(template_name, template_data):
    message = fill_template(template_name, template_data)
    
    # print('=======================')
    # print('MESSAGE')
    # print('=======================')
    # print(message)

    response = __get_ai_response(message)
    # print('=======================')
    # print('RESPONSE')
    # print('=======================')
    # print(response)

    return response

def fill_template(template_name: str, template_data: dict):
    env = Environment(loader=FileSystemLoader('app/templates'))
    template = env.get_template(f'{template_name}.j2')
    return template.render(**template_data)