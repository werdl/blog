import markdown
import json
import datetime


def load_from(file):
    """Load `file`'s contents into the blog management system"""
    with open(file, 'r') as f:
        lines = f.readlines()
        title = lines[0].strip()
        body = ''.join(lines[1:])
        # date is last modified date, formatted DD/MM/YYYY HH:MM:SS
        date = os.path.getmtime(file)
        fdate = datetime.datetime.fromtimestamp(date).strftime('%d/%m/%Y %H:%M:%S')

    # the first line is the article title
    # the rest is the article body

    # convert the body to HTML
    body = markdown.markdown(body)

    # add the head, and wrap body
    head = f"""
    <head>
        <title>{title}</title>
        <link rel="stylesheet" href="../style.css">
        <!-- jetbrains mono font -->
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap">
        <script src="../index.js"></script>
    </head>
    """
    
    html = f"""
    <!DOCTYPE html>
    <html>
        {head}
        <body>
            <h1>{title}</h1>
            <p>{fdate}</p>
            {body}
        </body>
    </html>
    """
    # write to new file in /articles
    with open(f'articles/{title}.html', 'w') as f:
        f.write(html)

    # add to posts.json
    if not os.path.exists('posts.json'):
        with open('posts.json', 'w') as f:
            json.dump([], f)
    with open('posts.json', 'r') as f:
        data = json.load(f)

    # search for all articles with the same title - if found, remove them
    data = [post for post in data if post['title'] != title]

    data.append({'title': title, 'file': f'articles/{title}.html', 'date': fdate})

    # write back to posts.json
    with open('posts.json', 'w') as f:
        json.dump(data, f)

    # generate index.html (list of articles)
    index_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Blog</title>
        <link rel="stylesheet" href="style.css">
        <!-- jetbrains mono font -->
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap">
        <script src="index.js"></script>
    </head>
    <body>
        <h1>Blog</h1>
        <ul>
    """
    for post in data:
        index_html += f'<li><a href="{post["file"]}">{post["title"]}</a> at {post["date"]}</li>'

    index_html += """
        </ul>
    </body>
    </html>
    """

    with open('index.html', 'w') as f:
        f.write(index_html)

    print('Done!')

# now take all files .md in /articles, and convert them to HTML
import os

for file in os.listdir('articles'):
    if file.endswith('.md'):
        load_from(f'articles/{file}')    
