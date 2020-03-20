import psycopg2
import os
from dotenv import load_dotenv
import sqlite3 as sql
from psycopg2.extras import execute_values

load_dotenv()

DB_NAME = os.getenv('DB_NAME', default='woops')
THIS_GUY = os.getenv('THIS_GUY', default='woops')
TREEHOUSE = os.getenv('TREEHOUSE', default='woops')
SERVER = os.getenv('SERVER', default='woops')

pg_conn = psycopg2.connect(dbname=DB_NAME,
                        user=THIS_GUY,
                        password=TREEHOUSE,
                        host=SERVER)
pg_curs = pg_conn.cursor()

rpg_conn = sql.connect('rpg_db.sqlite3')
rpg_curs = rpg_conn.cursor()

table = '''
CREATE TABLE Rpg_characters (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    level INTEGER NOT NULL,
    exp INTEGER NOT NULL,
    hp INTEGER NOT NULL,
    strength INTEGER NOT NULL,
    intelligence INTEGER NOT NULL,
    dexterity INTEGER NOT NULL,
    wisdom INTEGER NOT NULL
);
'''

pg_curs.execute(table)
pg_conn.commit()

rpg_curs.execute('SELECT * from charactercreator_character;')
data = rpg_curs.fetchall()

insert_query = '''
INSERT INTO Rpg_characters(
    character_id, name, level, exp, hp, strength, intelligence,
    dexterity, wisdom
)
VALUES %s;
'''

execute_values(pg_curs, insert_query, data)
pg_curs.execute('SELECT * FROM Rpg_characters')
result = pg_curs.fetchall()
print('RESULT: ', result)

pg_curs.close()
pg_conn.commit()

rpg_curs.close()
rpg_conn.commit()