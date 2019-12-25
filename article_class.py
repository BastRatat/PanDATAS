class Article:

    def __init__(self, title, post_date, author, content):
        self.title = title
        self.post_date = post_date
        self.author = author
        self.content = content

    def __repr__(self):
        return f"Article('title: {self.title}'\r'post_date: {self.post_date}'\r'author: {self.author}'\r'content: {self.content}')"
