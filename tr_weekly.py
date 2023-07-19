import whisper
import openai
import os
from scribe import send_notes
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    transcript = transcribe('tr_weekly.mp4')
    res = summarize(transcript)
    with open('result.txt', 'w') as file:
        file.write(res)
    send_notes(res)

# Load medium english only model and transcribe
def transcribe(recording):
    model = whisper.load_model("medium.en")
    result = model.transcribe(recording)

    return result["text"]

def summarize(transcript):

    # Grab system prompt from system.txt
    with open('system.txt') as f:
        system_prompt = f.read()

    # Grab sample output
    with open('sample.txt') as f:
        sample_txt = f.read()
    
    print(system_prompt)

    response = openai.ChatCompletion.create(   
        model="gpt-3.5-turbo-16k",
        messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": transcript},
            ]
        )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    main()
