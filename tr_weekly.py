import whisper
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    transcript = transcribe('recording.mp4')
    res = summarize(transcript)

# Load base english only model and transcribe
def transcribe(recording):
    model = whisper.load_model("base.en")
    result = model.transcribe(recording)

    return result["text"]

def summarize(transcript):

    # Grab system prompt from system.txt
    with open('system.txt') as f:
        system_prompt = f.read()

    print(system_prompt)

    # response = openai.ChatCompletion.create(   
    #     model="gpt-3.5-turbo",
    #     messages=[
    #             {"role": "system", "content": system_prompt},
    #             {"role": "user", "content": "Who won the world series in 2020?"},
    #             {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    #             {"role": "user", "content": "Where was it played?"}
    #         ]
    #     )
    # return response

if __name__ == "__main__":
    main()
