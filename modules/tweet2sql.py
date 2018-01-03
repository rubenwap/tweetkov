import psycopg2
import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)
conn = psycopg2.connect("dbname={dbname} user={user} host={host} port={port}".format(dbname=os.getenv(
    "dbname"), user=os.getenv("dbuser"), host=os.getenv("dbhost"), port=os.getenv("dbport")))

def read_tl(handle):
    cur = conn.cursor()
    cur.execute(
        "SELECT key, handle, tl FROM ruben.tweetkov.full_tl WHERE handle = '{}';".format(handle.lower()))
    return cur.fetchone()

def write_tl(handle, tl):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ruben.tweetkov.full_tl (handle, tl) VALUES (%s,%s)", (handle.lower(), tl))
    conn.commit()
    return read_tl(handle)


