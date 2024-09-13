# main.py 파일
import feedparser
import time
import requests

URL = "https://star-peanuts.tistory.com/rss"
headers = {'Cache-Control': 'no-cache'}
response = requests.get(URL, headers=headers)
RSS_FEED = feedparser.parse(response.content)

MAX_POST = 7

markdown_text = """
<div align=start>
  <p> Welcome to My github😄 <br>I’m majoring in computer science</p>
</div>

## ✨ Platforms & Languages
<img src="https://img.shields.io/badge/Java-007396?style=flat&logo=Conda-Forge&logoColor=white" />&nbsp;
<img src="https://img.shields.io/badge/python-3776AB?style=flat&logo=python&logoColor=white" />&nbsp;
<img src="https://img.shields.io/badge/Dart-0175C2?style=flat&logo=Dart&logoColor=white" />&nbsp;
<br>
<img src="https://img.shields.io/badge/Spring-6DB33F?style=flat&logo=Spring&logoColor=green" />&nbsp;
<img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=Django&logoColor=white" />&nbsp;
<img src="https://img.shields.io/badge/Flutter-02569B?style=flat&logo=Flutter&logoColor=white" />&nbsp;
<img src="https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=MySQL&logoColor=white" />

## 💬 Contact me!
<div align=start>
	<a href="https://star-peanuts.tistory.com">
		<img src="https://img.shields.io/badge/Blog-FF9800?style=flat&logo=Blogger&logoColor=white" />
	</a>
	<a href="mailto:jia5232@kookmin.ac.kr">
		<img src="https://img.shields.io/badge/Mail-30B980?style=flat&logo=Gmail&logoColor=white" />
	</a>
	<br>
</div>

## ✅ Latest Blog Post

"""  # list of blog posts will be appended here

# 피드 데이터가 비어있을 경우의 처리 추가
if 'entries' in RSS_FEED:
    for idx, feed in enumerate(RSS_FEED['entries']):
        if idx >= MAX_POST:
            break
        else:
            feed_date = feed.get('published_parsed')
            # 'published_parsed'가 없을 경우 처리
            if feed_date:
                formatted_date = time.strftime('%Y/%m/%d', feed_date)
            else:
                formatted_date = 'Unknown Date'

            title = feed.get('title', 'No Title')
            link = feed.get('link', '#')

            markdown_text += f"[{formatted_date} - {title}]({link}) <br/>\n<br/>\n"

# 기존 README 파일의 내용을 읽어옵니다.
try:
    with open("README.md", "r", encoding="utf-8") as f:
        old_content = f.read()
except FileNotFoundError:
    old_content = ""

# 새로운 내용이 기존 내용과 다를 때만 업데이트
if markdown_text != old_content:
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(markdown_text)
