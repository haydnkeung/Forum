# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach
# POSTS = [("This is the first post.", datetime.datetime.now())]
DBNAME = "forum"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  cursor = db.cursor()
  query = "SELECT content,time FROM posts ORDER BY time desc;"
  cursor.execute(query)
  posts = cursor.fetchall()
  db.close()
  return posts


def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database=DBNAME)
  cursor = db.cursor()
  cursor.execute("insert into posts values (%s)", (bleach.clean(content),))
  db.commit()
  db.close()


  # POSTS.append((content, datetime.datetime.now()))


