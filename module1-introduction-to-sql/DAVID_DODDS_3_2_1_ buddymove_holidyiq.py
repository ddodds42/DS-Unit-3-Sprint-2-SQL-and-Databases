import sqlite3 as sql
import pandas as pd

df = pd.read_csv('buddymove_holidayiq.csv')
df0 = df.rename({'User Id':'user_id'}, axis='columns')

conn = sql.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

df0.to_sql('reviews', con=conn, if_exists='replace')

# Question 1: Count how many rows you have - it should be 249!
query = '''
SELECT
COUNT(DISTINCT "index")
FROM reviews r;
'''

result = curs.execute(query).fetchall()
print('\n Question 1: Count how many rows you have - it should be 249!')
print(f'There are {result[0][0]} rows \n')

# Question 2: How many users who reviewed at least 100 Nature in the
# category also reviewed at least 100 in the Shopping category?
query0 = '''
SELECT
COUNT(DISTINCT "index")
FROM reviews r
WHERE Nature >= 100 AND Shopping >= 100
;
'''

result0 = curs.execute(query0).fetchall()
print('Question 2: How many users who reviewed at least 100 Nature in',
'the category also reviewed at least 100 in the Shopping category?')
print(f'{result0[0][0]} users reviewed at least 100 nature attractions and',
'100 shopping attractions. \n')

curs.close()
conn.commit()