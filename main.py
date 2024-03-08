import requests
import json
from openai import OpenAI

def load_config(filename='config.json'):
    with open(filename, 'r') as config_file:
        return json.load(config_file)

def autogen_message(messages, header):
    return f"{header}\n{''.join(messages)}"

def request_messages(token, channel_id):
    config_data = load_config()
    api = config_data.get('Api_Gpt', '')
    client = OpenAI(api_key=api)

    headers = {
        'Authorization': token
    }

    messages = []
    last_message_id = None

    while True:
        params = {
            'limit': 100,  # Maximum number of messages per request
            'before': last_message_id  # Retrieve messages before the last retrieved message
        }

        r = requests.get(f'http://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, params=params)

        if r.status_code != 200:
            print(f"Error retrieving messages. Status code: {r.status_code}")
            break

        json_data = json.loads(r.text)
        if not json_data:
            break  # No more messages

        messages.extend([message['content'] for message in json_data])
        last_message_id = json_data[-1]['id']

    # Generate message using autogen
    header = "Realiza un resumen de los mensajes del chat como un párrafo lo suficientemente extenso con lo importante y en otro apartado abajo del resumen menciona las palabras clave\n"
    autogen_msg = autogen_message(messages, header)

    gpt_request(client, autogen_msg)

def gpt_request(client, messages_text):
    # Use OpenAI GPT-3 API to generate a summary
    completions = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": messages_text
            }
        ],
        model="gpt-3.5-turbo"
    )
    print(completions.choices[0].message.content)

if __name__ == "__main__":
    config_data = load_config()
    token = config_data.get('token', '')
    channel_id = config_data.get('channel_id', '')

    if token and channel_id:
        request_messages(token, channel_id)
    else:
        print('Por favor, proporciona un token y un channel_id válidos en el archivo de configuración.')

