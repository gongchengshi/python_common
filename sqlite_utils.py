import StringIO
import sqlite3


def get_schema(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT * from sqlite_master')
    schema_file = StringIO.StringIO()
    for row in c.fetchall():
        schema_file.write('|'.join(row) + '\n')
    return schema_file.read()


def compare(db_path_1, db_path_2):
    schema_1 = get_schema(db_path_1)
    schema_2 = get_schema(db_path_2)
