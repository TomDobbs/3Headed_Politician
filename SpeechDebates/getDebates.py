# Aditi Raval, Trump Bot, (2015), trump-bot, https://github.com/araval/trump-bot
from bs4 import BeautifulSoup
from substitutions import *
import requests

#*********************************************************
#    Scrape for debates/speeches, clean them, and output to file
#*********************************************************
'''
ALL DEBATES OR SPEAKER TRANSCRIPTS ARE FROM HERE
'''

def get_debate(url, name, debate=1):
    r = requests.get(url)
    tmp = BeautifulSoup(r.text, 'html.parser')

    debate = []
    check = []
    name_flag = False

    for t in tmp.select('div p'):
        line = t.text
        soup = BeautifulSoup(line)
        line = soup.getText()
        line = line.encode('utf-8', 'ignore')
        line = deal_with_unicode(line)

        if debate == 1:
            if line.startswith(name) :
                name_flag = True
                line = ' '.join(line.split()[1:])
                line.strip()
                if not line.startswith("...") and len(line.split()) > 4 :
                    debate.append(line)
            elif line.split()[0].isupper() and line.split()[0] <> "(APPLAUSE)":
                name_flag = False
            elif name_flag:
                line.strip()
                if len(line.split()) > 4:
                    debate.append(line)
            else:
                check.append(line)

        else:
            # if line.split()[0].isupper() and line.split()[0] <> "(APPLAUSE)":
            #     name_flag = False
            # elif line.split()[0].isupper() and line.split()[0] <> "(CHEERS, APPLAUSE)":
            #     name_flag = False
            # elif line.split()[0].isupper() and line.split()[0] <> "(LAUGHTER)":
            #     name_flag = False
            # else:
            name_flag = True
            line = ' '.join(line.split()[1:])
            line.strip()
            if not line.startswith("...") and len(line.split()) > 4 :
                debate.append(line)

    return debate

# TRUMP SPEECHES
DT_url1 = "http://time.com/4267058/donald-trump-aipac-speech-transcript/"
DT_url2 = "http://time.com/4309786/read-donald-trumps-america-first-foreign-policy-speech/"
#DT_url3 = "http://time.com/4245134/super-tuesday-donald-trump-victory-speech-transcript-full-text/"
# REPUBLIC DEBATES
R_url1 = "http://time.com/3988276/republican-debate-primetime-transcript-full-text/"
R_url2 = "http://time.com/4037239/second-republican-debate-transcript-cnn/"
R_url3 = "http://time.com/4091301/republican-debate-transcript-cnbc-boulder/"
R_url4 = "http://time.com/4107636/transcript-read-the-full-text-of-the-fourth-republican-debate-in-milwaukee/"
R_url5 = "http://time.com/4150816/republican-debate-las-vegas-transcript/"
R_url6 = "http://time.com/4182096/republican-debate-charleston-transcript-full-text/"
#R_url7 = "" #Could not find
R_url8 = "http://time.com/4210921/republican-debate-transcript-new-hampshire-eighth/"
R_url9 = "http://time.com/4224275/republican-debate-transcript-south-carolina-ninth/"
R_url10 = "http://time.com/4238363/republican-debate-tenth-houston-cnn-telemundo-transcript-full-text/"
R_url11 = "http://time.com/4247496/republican-debate-transcript-eleventh-detroit-fox-news/"
R_url12 = "http://time.com/4255181/republican-debate-transcript-twelfth-cnn-miami/"

# DEMOCRATIC SPEECHES
HC_url1 = 'http://time.com/4265947/hillary-clinton-aipac-speech-transcript/'
HC_url2 = "http://time.com/4120295/hillary-clinton-foreign-policy-isis/"
BS_url1 = "http://time.com/4244244/bernie-sanders-super-tuesday-speech-transcript-full-text/"
BS_url2 = "http://time.com/4296102/bernie-sanders-vatican-speech-transcript/"
# DEMOCRATIC DEBATES
D_url1 = "http://time.com/4072553/democratic-debate-transcript-primetime-cnn/"
D_url2 = "http://time.com/4113434/transcript-read-the-full-text-of-the-second-democratic-debate/"
D_url3 = "http://time.com/4156144/democratic-debate-third-new-hampshire-abc-transcript/"
D_url4 = "http://time.com/4183952/democratic-debate-full-text-hillary-clinton-bernie-sanders/"
D_url5 = "http://time.com/4208869/democratic-debate-transcript-full-text-new-hampshire-fifth/"
D_url6 = "http://time.com/4218812/democratic-debate-transcript-full-text-milwaukee-sixth/"
D_url7 = "http://time.com/4249183/democratic-debate-flint-full-text-transcript-seventh/"
D_url8 = "http://time.com/4253623/democratic-debate-eighth-miami-transcript-full-text/"
D_url9 = "http://time.com/4295548/democratic-debate-ninth-brooklyn-transcript-full-text/"

# TRUMP SPEECHES
DT_speech1 = get_debate(DT_url1, 'TRUMP', debate=0)
DT_speech2 = get_debate(DT_url2, 'TRUMP', debate=0)
#DT_speech3 = get_debate(DT_url3, 'TRUMP', debate=1)
DT_debate1 = get_debate(R_url1, 'TRUMP', debate=1)
DT_debate2 = get_debate(R_url2, 'TRUMP', debate=1)
DT_debate3 = get_debate(R_url3, 'TRUMP', debate=1)
DT_debate4 = get_debate(R_url4, 'TRUMP', debate=1)
DT_debate5 = get_debate(R_url5, 'TRUMP', debate=1)
DT_debate6 = get_debate(R_url6, 'TRUMP', debate=1)
#DT_debate7 = get_debate(R_url7, 'TRUMP', debate=1)
DT_debate8 = get_debate(R_url8, 'TRUMP', debate=1)
DT_debate9 = get_debate(R_url9, 'TRUMP', debate=1)
DT_debate10 = get_debate(R_url10, 'TRUMP', debate=1)
DT_debate11 = get_debate(R_url11, 'TRUMP', debate=1)
DT_debate12 = get_debate(R_url12, 'TRUMP', debate=1)

# CLINTON SPEECHES
HC_speech1 = get_debate(HC_url1, "HILLARY", debate=0)
HC_speech2 = get_debate(HC_url2, "HILLARY", debate=0)
HC_debate1 = get_debate(D_url1, "HILLARY", debate=1)
HC_debate2 = get_debate(D_url2, "HILLARY", debate=1)
HC_debate3 = get_debate(D_url3, "HILLARY", debate=1)
HC_debate4 = get_debate(D_url4, "HILLARY", debate=1)
HC_debate5 = get_debate(D_url5, "HILLARY", debate=1)
HC_debate6 = get_debate(D_url6, "HILLARY", debate=1)
HC_debate7 = get_debate(D_url7, "HILLARY", debate=1)
HC_debate8 = get_debate(D_url8, "HILLARY", debate=1)
HC_debate9 = get_debate(D_url9, "HILLARY", debate=1)

# SANDERS SPEECHES
BS_speech1 = get_debate(BS_url1, "SANDERS", debate=1)
BS_speech2 = get_debate(BS_url2, "SANDERS", debate=0)
BS_debate1 = get_debate(D_url1, "SANDERS", debate=1)
BS_debate2 = get_debate(D_url2, "SANDERS", debate=1)
BS_debate3 = get_debate(D_url3, "SANDERS", debate=1)
BS_debate4 = get_debate(D_url4, "SANDERS", debate=1)
BS_debate5 = get_debate(D_url5, "SANDERS", debate=1)
BS_debate6 = get_debate(D_url6, "SANDERS", debate=1)
BS_debate7 = get_debate(D_url7, "SANDERS", debate=1)
BS_debate8 = get_debate(D_url8, "SANDERS", debate=1)
BS_debate9 = get_debate(D_url9, "SANDERS", debate=1)

'''
The fourth debate is from a different website, so the scraping is a bit
different
'''

url = "http://www.nytimes.com/2015/11/11/us/politics/ \
       transcript-republican-presidential-debate.html?_r=0"
r = requests.get(url)
tmp = BeautifulSoup(r.text, 'html.parser')

DT_debate4 = []
check = []
trump_flag = False
for t in tmp.select('div p'):
    soup = BeautifulSoup(t.text)
    line = soup.getText()
    line = line.encode('utf-8', 'ignore')
    line = deal_with_unicode(line)

    if line <> 'Advertisement':
        if line.startswith('TRUMP') :
            trump_flag = True
            line = ' '.join(line.split()[1:])
            line.strip()
            if not line.startswith("...") and len(line.split()) > 3 :
                debate4.append(line)
        elif line.split()[0].isupper():
            trump_flag = False
        elif trump_flag:
            line.strip()
            debate4.append(str(trump_flag) + ' ' + line)
        else:
            check.append(line)

#********************************************
# Write debates to file:
#********************************************

def write_lines(f, debate):
    for line in debate:
        line = make_substitutions(line, ignore_ascii=0)
        line = line + '\n'
        f.write(line)


donald_transcripts = [ DT_speech1, DT_speech2, DT_debate1, \
                    DT_debate2, DT_debate3, DT_debate4, DT_debate5, \
                    DT_debate6, DT_debate8, DT_debate9, \
                    DT_debate10, DT_debate11, DT_debate12 ]

sanders_transcripts = [ BS_speech1, BS_speech2, BS_debate1, BS_debate2, \
                    BS_debate3, BS_debate4, BS_debate5, BS_debate6, \
                    BS_debate7, BS_debate8, BS_debate9 ]

clinton_transcripts = [ HC_speech1, HC_speech2, HC_debate1, HC_debate2, \
                    HC_debate3, HC_debate4, HC_debate5, HC_debate6, \
                    HC_debate7, HC_debate8, HC_debate9 ]

with open('Total_Speeches.txt', 'w') as f:
    for transcript in donald_transcripts:
        write_lines(f, transcript)
    for transcript in sanders_transcripts:
        write_lines(f, transcript)
    for transcript in clinton_transcripts:
        write_lines(f, transcript)

with open('Trump_speeches.txt', 'w') as f:
    for transcript in donald_transcripts:
        write_lines(f, transcript)

with open('Clinton_speeches.txt', 'w') as f:
    for transcript in clinton_transcripts:
        write_lines(f, transcript)

with open('Sanders_speeches.txt', 'w') as f:
    for transcript in sanders_transcripts:
        write_lines(f, transcript)


#********************************************
#  DONE
#********************************************
