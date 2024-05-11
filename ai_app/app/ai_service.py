import os

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# model = 'mistral-large-latest'
model = 'open-mixtral-8x22b'

client = MistralClient(api_key=os.environ.get('AI_API_KEY'))

def get_ai_response(message):
    messages = [
        ChatMessage(role='user', content=message)
    ]

    chat_response = client.chat(
        model=model,
        response_format={'type': 'json_object'},
        messages=messages,
    )

    response = chat_response.choices[0].message.content
    print(response)
    return response


# get_ai_response('Return "Hello" using the list in JSON-format')