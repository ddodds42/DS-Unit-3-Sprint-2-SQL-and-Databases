import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('DB_NAME', default='woops')
THIS_GUY = os.getenv('THIS_GUY', default='woops')
TREEHOUSE = os.getenv('TREEHOUSE', default='woops')
SERVER = os.getenv('SERVER', default='woops')

conn = psycopg2.connect(dbname=DB_NAME,
                        user=THIS_GUY,
                        password=TREEHOUSE,
                        host=SERVER)

curs = conn.cursor()

curs.execute('SELECT * from toy_table;')

result = curs.fetchone()
print('RESULT: ', result)