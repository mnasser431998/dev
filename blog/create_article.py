import os

article_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="../css/styles.css">
</head>
<body>
    <header>
        <h1>{title}</h1>
        <nav>
            <ul>
                <li><a href="../index.html">Home</a></li>
                <li><a href="../about.html">About</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <p>{content}</p>
    </main>
</body>
</html>
'''

articles = [
    {"title": "Article 1", "content": "This is the content of Article 1."},
    {"title": "Article 2", "content": "This is the content of Article 2."},
]

os.makedirs('blog', exist_ok=True)

for article in articles:
    with open(f"blog/{article['title'].replace(' ', '_').lower()}.html", 'w') as f:
        f.write(article_template.format(title=article['title'], content=article['content']))
