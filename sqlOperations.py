import sqlite3

def insertIntoTable():
    # os.chdir(r"..")
    con = sqlite3.connect("checksums.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE dirpath, dirname, filename")