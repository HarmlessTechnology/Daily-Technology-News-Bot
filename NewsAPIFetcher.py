# Daily Tech News Bot - NEWS API FETCHER/CONTENT WRITER
#V0.1

import pprint # DEBUG
import requests
from datetime import date
from datetime import timedelta
import json

# Define yesterdays date
yesterday = date.today() - timedelta(days=2)
# Define number of articles for each source
articleNum = 1
# define language
lang = 'en'

# Define access and API key
APIkey = "*******************************"
url = 'https://newsapi.org/v2/top-headlines'

# Request parameters TechRadar
parameters1 = {
    'sources': 'techradar',  # source
    'language': lang,  # language
    'pageSize': articleNum,  # max 100
    'from': yesterday,  # Time period
    'apiKey': APIkey  # API Key
}

# Request parameters IGN
parameters2 = {
    'sources': 'ign',  # source
    'language': lang,  # language
    'pageSize': articleNum,  # max 100
    'from': yesterday,  # Time period
    'apiKey': APIkey  # API Key
}

# Request parameters The Verge
parameters3 = {
    'sources': 'the-verge',  # source
    'language': lang,  # language
    'pageSize': articleNum,  # max 100
    'from': yesterday,  # Time period
    'apiKey': APIkey  # API Key
}

# Request parameters Wired
parameters4 = {
    'sources': 'wired',  # source
    'language': lang,  # language
    'pageSize': articleNum,  # max 100
    'from': yesterday,  # Time period
    'apiKey': APIkey  # API Key
}

# Request news
response1 = requests.get(url, params=parameters1)
response2 = requests.get(url, params=parameters2)
response3 = requests.get(url, params=parameters3)
response4 = requests.get(url, params=parameters4)

# Gather responses as jsons
response1_json = response1.json()
response2_json = response2.json()
response3_json = response3.json()
response4_json = response4.json()

# Print responses (DEBUG)
pprint.pprint(response1_json)
pprint.pprint(response2_json)
pprint.pprint(response3_json)
pprint.pprint(response4_json)

# Write all data to .json files (This will overwrite the existing json every run)
with open("response1.json", "w") as outfile:
    json.dump(response1_json, outfile)
with open("response2.json", "w") as outfile:
    json.dump(response2_json, outfile)
with open("response3.json", "w") as outfile:
    json.dump(response3_json, outfile)
with open("response4.json", "w") as outfile:
    json.dump(response4_json, outfile)

# Create text file of article summary (This will overwrite the existing text file every run)
try:
    with open('response1.json', 'r') as article1:
        articleContent1 = json.load(article1)
        for c1 in articleContent1['articles']:
            title = c1['title']
            content = c1['content']
            url = c1['url']
    art1 = open('article1.txt', 'w')
    art1.write(str(title)+'\n'+str(content)+'\n'+str(url))
    art1.close()
except ValueError:
    pass

try:
    with open('response2.json', 'r') as article2:
        articleContent2 = json.load(article2)
        for c2 in articleContent2['articles']:
            title = c2['title']
            content = c2['content']
            url = c2['url']
    art2 = open('article2.txt', 'w')
    art2.write(str(title)+'\n'+str(content)+'\n'+str(url))
    art2.close()
except ValueError:
    pass

try:
    with open('response3.json', 'r') as article3:
        articleContent3 = json.load(article3)
        for c3 in articleContent3['articles']:
            title = c3['title']
            content = c3['content']
            url = c3['url']
    art3 = open('article3.txt', 'w')
    art3.write(str(title)+'\n'+str(content)+'\n'+str(url))
    art3.close()
except ValueError:
    pass

try:
    with open('response4.json', 'r') as article4:
        articleContent4 = json.load(article4)
        for c4 in articleContent4['articles']:
            title = c4['title']
            content = c4['content']
            url = c4['url']
    art4 = open('article4.txt', 'w')
    art4.write(str(title)+'\n'+str(content)+'\n'+str(url))
    art4.close()
except ValueError:
    pass

# Merge all articles into one text file for reading
data1 = data2 = data3 = data4 = ""

with open('article1.txt') as fp:
    data1 = fp.read()
with open('article2.txt') as fp:
    data2 = fp.read()
with open('article3.txt') as fp:
    data3 = fp.read()
with open('article4.txt') as fp:
    data4 = fp.read()

data1 += "\r\n"
data1 += data2
data1 += "\r\n"
data1 += data3
data1 += "\r\n"
data1 += data4

with open('completeArticle.txt', 'w') as fp:
    fp.write(data1)
