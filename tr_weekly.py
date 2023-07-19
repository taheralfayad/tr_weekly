import os
import subprocess
import time
import openai

from dotenv import load_dotenv

load_dotenv()

process = subprocess.run(['whisper', 'tr_weekly.mp4', '--model', 'medium.en'], stdout=subprocess.PIPE, text=True)

time.sleep(5)

openai.api_key = os.getenv("OPENAI_API_KEY")

with open("tr_weekly.txt", "r") as file:
    data = file.read()

format = """
:pighappy: TR WEEKLY: :pighappy:
:trumpet: ANNOUNCEMENTS :trumpet:
*Insert a summary of announcements
:bar_chart:Performance Insights:
*Insert summary of performance insights
:techrangers-wave:TR Outreach:
*Insert summary of TR outreach
:female_vampire:Vampire:
*Insert summary of Vampire content
:closed_book:Course Dev & Pressbooks:
*Insert summary of Course Dev & Pressbooks
:materia: Materia: :peario:
*Insert summary of Materia
:obojobo:OBOJOBO:
*Insert summary of Obojobo
:spider_web: WORDPRESS:
*Insert summary of Wordpress
:apcfrog: Captioning :frog::
*Insert summary of Captioning
:quality:Quality Badges:
*Insert summary of Quality Badges
:udoit:UDOIT:
*Insert summary of UDOIT
:party-patch:Soulpatch:
*Insert summary of Materia
:canvas: LTI 1.3 Conversion:
*Insert summary of LTI 1.3 Conversion
:ucfhere: UCFHere :ucfhere::
*Insert summary of UCFhere
:jack_o_lantern:THE PUMPKIN: *Insert pumpkin question.
*Insert pumpkin question answers """

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-16k-0613",
  messages=[
        {"role": "user", "content": "Summarize the following text in this format with bullet points." + format},
        {"role": "user", "content": data}
    ]
)

print(response['choices'][0]['message']['content'])
