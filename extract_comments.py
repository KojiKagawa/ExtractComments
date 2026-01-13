from bs4 import BeautifulSoup, Comment
import requests
import sys

def extract_comments(content):
    soup = BeautifulSoup(content, 'html.parser')
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    return [comment.strip() for comment in comments]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extractComments.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    if url.startswith('http://') or url.startswith('https://'):
        response = requests.get(url)
        if response.status_code == 200:
            content = response.content
            comments = extract_comments(content)
            for comment in comments:
                print(comment)
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    else:
        # Assume it's a local file path
        with open(url, 'r', encoding='utf-8') as file:
            content = file.read()
            comments = extract_comments(content)
            for comment in comments:
                print(comment)