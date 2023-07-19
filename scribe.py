import requests
import json
from dotenv import load_dotenv
import os

def send_notes(notes):
    load_dotenv()

    # Bot User OAuth Access Token
    token = os.getenv("SLACK_API")

    # Channel to send the message to
    channel_id = os.getenv("CHANNEL_ID")

    headers = {
        'Content-type': 'application/json', 
        'Authorization': 'Bearer {}'.format(token)
    }

    data = {
        'channel': channel_id,
        'text': notes,
    }

    response = requests.post('https://slack.com/api/chat.postMessage', 
                            headers=headers, 
                            data=json.dumps(data))
