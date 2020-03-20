import psycopg2
import os
from dotenv import load_dotenv
import sqlite3 as sql
from psycopg2.extras import execute_values
import pandas as pd

filepath = os.path.join(
    os.path.dirname(
        __file__
    ),
    "..", 'titanic.csv'
)

df = pd.read_csv(filepath)
cols = ['Survived','Pclass','Name','Sex','Age','Sibs_Spouses_Aboard',
        'Parents_Children_Aboard','Fare']
df.columns= cols
print(df.dtypes)

load_dotenv()

DB_NAME = os.getenv('DB_NAME', default='woops')
THIS_GUY = os.getenv('THIS_GUY', default='woops')
TREEHOUSE = os.getenv('TREEHOUSE', default='woops')
SERVER = os.getenv('SERVER', default='woops')

tpg_conn = psycopg2.connect(dbname=DB_NAME,
                        user=THIS_GUY,
                        password=TREEHOUSE,
                        host=SERVER)
tpg_curs = tpg_conn.cursor()

the_data = list(df.itertuples(index=False, name=None))

table = '''
CREATE TABLE Rms_titanic1 (
    Survived INTEGER NOT NULL,
    Pclass INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    Sex VARCHAR(10) NOT NULL,
    Age REAL NOT NULL,
    Sibs_Spouses_Aboard INTEGER NOT NULL,
    Parents_Children_Aboard INTEGER NOT NULL,
    Fare REAL NOT NULL
);
'''
# character_id SERIAL PRIMARY KEY,

tpg_curs.execute(table)
tpg_conn.commit()

insert_query = '''
INSERT INTO Rms_titanic1 (
    Survived, Pclass, Name, Sex, Age, Sibs_Spouses_Aboard,
    Parents_Children_Aboard, Fare
)
VALUES %s;
'''

execute_values(tpg_curs, insert_query, the_data)
tpg_curs.execute('SELECT * FROM Rms_titanic1')
result = tpg_curs.fetchone()
print('RESULT: ', result)

tpg_curs.close()
tpg_conn.commit()