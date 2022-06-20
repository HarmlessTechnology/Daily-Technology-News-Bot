# Daily Tech News Bot - WORDPRESS POST CREATOR
#V0.1

import requests
import json
import base64
from datetime import date
import NewsAPIFetcher

# -POST VARIABLES-    https://developer.wordpress.org/rest-api/reference/posts/#create-a-post
now = date.today()  # TODAY'S DATE
date = str(now) + 'T06:00:00'  # DATE, DO NOT CHANGE
slug = 'dtn-' + str(now)  # SLUG, DO NOT CHANGE
title = 'Daily Technology News Summary: ' + str(now)  # TITLE
status = 'publish'  # STATUS, 'private', 'publish'
author = '0'  # AUTHOR, DO NOT CHANGE
formatting = 'standard'  # FORMAT
summary = "Today's tech news summary!"  # EXCERPT

# IMPORT POST CONTENT
exec('NewsAPIFetcher')
completeArticle = open('completeArticle.txt', 'r')
content = "For today's daily tech news summary: " + '\r\n' + '\r\n' + completeArticle.read() + '\r\n' + '\r\n' + \
          'Articles are the sole property of their respective publishers. ' \
          'Content gathered by Harmless Technology for user convenience.' + '\r\n' + "That " \
                                                                                     "concludes today's tech news." \
                                                                                     " New daily tech news is posted " \
                                                                                     "every morning!"
completeArticle.close()

# -CREDENTIALS-
user = '********************'  # USERNAME
pythonapp = '*****************'  # APPLICATION PASSWORD
url = '*****************************'  # JSON URL
creds = user + ':' + pythonapp  # COMBINE CREDENTIALS
token = base64.b64encode(creds.encode())  # ENCODE CREDENTIALS
headers = {'Authorization': 'Basic ' + token.decode('utf-8')}  # CREATE HEADER

# -POST-
post = {'date': date,  # PUBLICATION DATE
        'title': title,  # TITLE
        'slug': slug,  # SLUG
        'status': status,  # POST STATUS
        'content': content,  # CONTENT
        'author': author,  # AUTHOR
        'excerpt': summary,  # EXCERPT
        'format': formatting,  # FORMAT
        'categories': 49
        }

# -VERIFICATION-
r = requests.post(url + '/posts', headers=headers, json=post)  # PUBLISH
print('POST PUBLISHED:  ' + json.loads(r.content)['link'])  # VERIFY
