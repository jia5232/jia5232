import feedparser, time

URL = "https://star-peanuts.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

def fetch_latest_blog_posts():
    markdown_text = ""
    for idx, feed in enumerate(RSS_FEED['entries']):
        if idx >= MAX_POST:
            break
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
    return markdown_text

def update_readme(latest_posts):
    with open("README.md", "r", encoding="utf-8") as readme:
        content = readme.read()

    start_marker = "<!-- BLOG-POST-LIST:START -->"
    end_marker = "<!-- BLOG-POST-LIST:END -->"
    start_idx = content.find(start_marker) + len(start_marker)
    end_idx = content.find(end_marker)

    new_content = content[:start_idx] + "\n" + latest_posts + content[end_idx:]

    with open("README.md", "w", encoding="utf-8") as readme:
        readme.write(new_content)

if __name__ == "__main__":
    latest_posts = fetch_latest_blog_posts()
    update_readme(latest_posts)
