import psycopg2

def read_tl(handle):
    conn = psycopg2.connect("dbname=ruben user=ruben host=localhost port=5432")
    cur = conn.cursor()
    cur.execute(
        "SELECT key, handle, tl FROM ruben.tweetkov.full_tl WHERE handle = '{}';".format(handle))
    return cur.fetchone()

def write_tl(handle, tl):

    conn = psycopg2.connect("dbname=ruben user=ruben host=localhost port=5432")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ruben.tweetkov.full_tl (handle, tl) VALUES (%s,%s)", (handle, tl))
    conn.commit()
    return read_tl(handle)


