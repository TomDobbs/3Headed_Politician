# Aditi Raval, Trump Bot, (2015), trump-bot, https://github.com/araval/trump-bot
from bs4 import BeautifulSoup
from substitutions import *
import os
import requests

'''
I have six files with speeches in my directory.
This part just cleans up the speeches.
'''

def clean_text(file):
    speeches = []
    for filename in os.listdir(os.getcwd()):
        if filename[:] == file:
            with open(filename) as f:
                speeches.append(f.readlines())

    cleanSpeech = []
    for speech in speeches:
        for line in speech:
            soup = BeautifulSoup(line)
            line = soup.getText()
            line = line.encode('ascii', 'ignore')
            line = line.strip()
            if len(line.split()) > 0:
                line = deal_with_unicode(line)
                line = make_substitutions(line)
                cleanSpeech.append(line)

    return cleanSpeech

Total_clean = clean_text('Total_Speeches.txt')
Sanders_clean = clean_text('Sanders_speeches.txt')
Clinton_clean = clean_text('Clinton_speeches.txt')
Trump_clean = clean_text('Trump_speeches.txt')

# Write cleaned Speeches to file
with open('Total_cleanSpeech.txt', 'w') as f:
    for sentence in Total_clean:
        sentence = sentence+'\n'
        f.write(sentence)

with open('Sanders_cleanSpeech.txt', 'w') as f:
    for sentence in Sanders_clean:
        sentence = sentence+'\n'
        f.write(sentence)

with open('Clinton_cleanSpeech.txt', 'w') as f:
    for sentence in Clinton_clean:
        sentence = sentence+'\n'
        f.write(sentence)

with open('Trump_cleanSpeech.txt', 'w') as f:
    for sentence in Trump_clean:
        sentence = sentence+'\n'
        f.write(sentence)
