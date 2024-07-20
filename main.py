import requests
from bs4 import BeautifulSoup

def fetch_blog_posts():
    url = "https://star-peanuts.tistory.com"  # Your blog URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    posts = []
    for item in soup.select("item selector for your blog posts"):  # Update with the actual CSS selector for your blog posts
        title = item.select_one("title selector").get_text()  # Update with the actual title selector
        link = item.select_one("link selector")["href"]  # Update with the actual link selector
        date = item.select_one("date selector").get_text()  # Update with the actual date selector
        posts.append(f"[{date} - {title}]({link})")

    return posts

def update_readme(posts):
    with open("README.md", "r") as file:
        readme_contents = file.readlines()

    start_marker = "<!-- BLOG-POST-LIST:START -->\n"
    end_marker = "<!-- BLOG-POST-LIST:END -->\n"

    start_index = readme_contents.index(start_marker) + 1
    end_index = readme_contents.index(end_marker)

    new_contents = readme_contents[:start_index] + [f"{post}\n" for post in posts[:5]] + readme_contents[end_index:]

    with open("README.md", "w") as file:
        file.writelines(new_contents)

if __name__ == "__main__":
    blog_posts = fetch_blog_posts()
    update_readme(blog_posts)
