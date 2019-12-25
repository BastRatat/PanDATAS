"""
Article database CRUD functions
24/12/2019
"""

import sqlite3
from article_class import Article

conn = sqlite3.connect('articles.db')

c = conn.cursor()


def insert_article(acl):
    dict_art = {
        "title": acl.title,
        "post_date": acl.post_date,
        "author": acl.author,
        "content": acl.content
    }

    with conn:
        c.execute(
            "INSERT INTO articles VALUES (:title, :post_date, :author, :content)", dict_art)


def read_by_title(title):
    with conn:
        c.execute("SELECT * FROM articles WHERE title=?", (title,))
        return c.fetchall()


def update_content(acl, new_content):
    new_dict = {'title': acl.title,
                'post_date': acl.post_date,
                'author': acl.author,
                'content': new_content}
    with conn:
        c.execute("""UPDATE articles SET content = :content
                     WHERE title = :title AND post_date = :post_date AND author = :author""", new_dict
                  )


def update_title(acl, new_title):
    new_dict = {'title': new_title,
                'post_date': acl.post_date,
                'author': acl.author,
                'content': acl.content}
    with conn:
        c.execute("""UPDATE articles SET title = :title
                     WHERE post_date = :post_date AND author = :author AND content = :content""", new_dict
                  )


def update_date(acl, new_date):
    new_dict = {'title': acl.title,
                'post_date': new_date,
                'author': acl.author,
                'content': acl.content}
    with conn:
        c.execute("""UPDATE articles SET post_date = :post_date
                     WHERE title = :title AND author = :author AND content = :content""", new_dict
                  )


def update_author(acl, new_author):
    new_dict = {'title': acl.title,
                'post_date': acl.post_date,
                'author': new_author,
                'content': acl.content}
    with conn:
        c.execute("""UPDATE articles SET author = :author
                     WHERE title = :title AND post_date = :post_date AND content = :content""", new_dict
                  )


def remove_article(acl):
    new_dict = {'title': acl.title,
                'post_date': acl.post_date,
                'author': acl.author,
                'content': acl.content}
    with conn:
        c.execute("DELETE from articles WHERE title = :title AND post_date = :post_date AND author = :author AND content = :content",
                  new_dict)


# c.execute('''CREATE TABLE articles
#     (title text,
#     post_date text,
#     author text,
#     content text)
#     ''')

first_post = Article('first post title', '25/12/2019', 'Bastien Ratat',
                     'first post content')


"""
DB MANAGEMENT TO BE DOWN BELOW
"""

conn.close()
