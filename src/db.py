import os

import psycopg2

def connect():
    return psycopg2.connect(
        host=os.environ['PGSQL_HOST'],
        port=os.environ['PGSQL_PORT'],
        user=os.environ['PGSQL_USER'],
        password=os.environ['PGSQL_PASSWORD'],
        dbname=os.environ['PGSQL_DBNAME'])
