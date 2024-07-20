import feedparser, time

URL = "https://star-peanuts.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 7

markdown_text = """
<div align=start>
  <p> Welcome to My github😄 <br>My name is Jia and I’m majoring in computer science at kookmin univ.🏫</p>
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

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

with open("README.md", mode="w", encoding="utf-8") as f:
    f.write(markdown_text)
