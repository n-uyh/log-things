import feedparser
import git
import os
from datetime import datetime

rss_url = 'https://api.velog.io/rss/@edocnuyh'

repo_path = '.'

posts_dir = os.path.join(repo_path, 'velog-posts')

if not os.path.exists(posts_dir):
  os.makedirs(posts_dir)

repo = git.Repo(repo_path)

feed = feedparser.parse(rss_url)

repo.git.checkout('logs')

for entry in feed.entries:
  file_name = entry.title
  file_name = file_name.replace('/', '-')
  file_name = file_name.replace('\\', '-')
  file_name += '.md'
  file_path = os.path.join(posts_dir, file_name)

  content = entry.description

  if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
      if file.read() == content:
        continue
        
  with open(file_path, 'w', encoding='utf-8') as file:
    file.write(content)

  repo.git.add(file_path)

current_date = datetime.now().strftime('%Y-%m-%d')
if repo.is_dirty():
  repo.git.commit('-m', f'Add posts from Velog on {current_date}')
  repo.git.push('--set-upstream', 'origin', 'logs')
else:
  print("No changes to commit")
