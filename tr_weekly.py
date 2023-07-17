import os
import subprocess
import time

process = subprocess.run(['whisper', 'tr_weekly.mp4', '--model', 'medium.en'], stdout=subprocess.PIPE, text=True)

time.sleep(5)

with open("tr_weekly.txt", "r") as file:
    data = file.read()


format = """
:pighappy: TR WEEKLY: :pighappy:
:trumpet: ANNOUNCEMENTS :trumpet:
*Insert a summary of all of the announcements here in bullet point format.
:bar_chart:Performance Insights:
*Insert everything related to performance insights here in bullet point format.
:techrangers-wave:TR Outreach:
*Insert a summary of all of the TR outreach here in bullet point format.
:female_vampire:Vampire:
*Insert a summary of all of the Vampire related content here in bullet point format.
:closed_book:Course Dev & Pressbooks:
*Insert a summary of all of the Course Dev & Pressbooks content here in bullet point format.
:materia: Materia: :peario:
*Insert a summary of all of the Materia related content here in bullet point format.
:obojobo:OBOJOBO:
*Insert a summary of all of the Obojobo related content here in bullet point format.
:spider_web: WORDPRESS:
*Insert a summary of all of the Wordpress related content here in bullet point format.
:apcfrog: Captioning :frog::
*Insert a summary of all of the Captioning related content here in bullet point format.
:quality:Quality Badges:
*Insert a summary of all of the Quality Badges related content here in bullet point format.
:udoit:UDOIT:
*Insert a summary of all of the UDOIT related content here in bullet point format.
:party-patch:Soulpatch:
*Insert a summary of all of the Materia related content here in bullet point format.
:canvas: LTI 1.3 Conversion:
*Insert a summary of all of the LTI 1.3 Conversion related content here in bullet point format.
:ucfhere: UCF Here :ucfhere::
*Insert a summary of all of the UCFhere related content here in bullet point format.
:jack_o_lantern:THE PUMPKIN: *Insert the pumpkin question here.
*Insert all of the answers to the pumpkin question here """
