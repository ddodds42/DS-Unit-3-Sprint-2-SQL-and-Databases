import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

woops = '''
DROP TABLE IF EXISTS demo;
'''

curs.execute(woops)

create = '''
CREATE TABLE IF NOT EXISTS demo (
    s VARCHAR(10)
    ,x INT
    ,y INT
);
'''

curs.execute(create)

insertion = '''
INSERT INTO demo (s,x,y)
VALUES
    ('g','3','9')
    ,('v','5','7')
    ,('f','8','7')
;
'''

curs.execute(insertion)

query = 'SELECT * FROM demo;'

table = curs.execute(query).fetchall()
print('\n', 'Voila! The demo table:')
print(table, '\n')

# Count how many rows you have - it should be 3!

query0 = '''
SELECT COUNT (*)
FROM demo;
'''

rows = curs.execute(query0).fetchall()
print('Count how many rows you have - it should be 3!')
print(f'The table has {rows[0][0]} rows. \n')

# How many rows are there where both x and y are at least 5?

query1 = '''
SELECT COUNT (*)
FROM demo
WHERE x>=5 AND y>=5;
'''

fives = curs.execute(query1).fetchall()
print('How many rows are there where both x and y are at least 5?')
print(f'There are {fives[0][0]} rows where both x and y are at least 5. \n')

# How many unique values of y are there?

query2 = '''
SELECT COUNT (DISTINCT d.y)
FROM demo d;
'''

yunq = curs.execute(query2).fetchone()
print('How many unique values of y are there?')
print(f'Column y has {yunq[0]} unique values. \n')

curs.close()
conn.commit()