import os
import subprocess
import time

process = subprocess.run(['whisper', 'tr_weekly.m4a', '--model', 'medium.en'], stdout=subprocess.PIPE, text=True)

time.sleep(5)

with open("tr_weekly.txt", "r") as file:
    data = file.read()


format = """
:pighappy:TR WEEKLY: :pighappy:
:trumpet: ANNOUNCEMENTS :trumpet:
Hackday Next week!
Kickoff at 10AM monday
Final decisions for new techrangers next week
Pancake breakfast 8:30-10:30AM on Wednesday
Final round for System Engineer II position next week
Soccer game today at 6
Fill out the climate survey
Due the 21st
:bar_chart:Performance Insights:
Email went out to say it is getting retired August 9th
:techrangers-wave:TR Outreach:
No updates
:female_vampire:Vampire:
temporary on hold.
:closed_book:Course Dev & Pressbooks:
Still working on bio book conversion
Some tickets for fall starting to come in
:materia: Materia: :peario:
Working on accessibility stuff
Corey is reviewing PRs from Cay and Brandon
:obojobo:OBOJOBO:
Morgan finished course based assessment stats
Viggie working on new border options
:spider_web: WORDPRESS:
Made change to prod with no issues
Websites are not accessible off campus/VPN
Related to UCF IT
:apcfrog: Captioning :frog::
Rev budget has been stabilized
Worked on integrating automated captions (robocaptioning)
I (Evan) have been writing tests for captionhub and working on lti issues with ableplayer
:quality:Quality Badges:
No updates
:udoit:UDOIT:
Taher working on PHP Ally stuff
Danny reviewing issues wth PRs
Possibly related to JWT stuff
:party-patch:Soulpatch:
Was down until late yesterday
Certificate for SSO expired, should be working now
No new development work
:canvas: LTI 1.3 Conversion:
Templater is running on EC2
Matt finished dev and prod dbs
Will be testing with syntax highlighter later
Me (Evan) and Danny working on LTI issues related to JWT from url
:ucfhere: UCF Here :ucfhere::
Emmanuel worked with Morgan on AWS/Docker configurations
:jack_o_lantern:THE PUMPKIN: If you were locked in a time machine set for a single one-way trip to the past or future and had 10 minutes to dial in the time and place, when and where would you go? Why?
Danny G - Go back an hour before to have more time to think how to use time machine
Danny M - Back in time to see dinosaurs as long as it's safe
Jacob - Late 80s computer shows
Me (Evan) - Go back 10 years and bet on sports games """

print(format)
