import sqlite3 as sql
import pandas as pd

conn = sql.connect('rpg_db.sqlite3')
print('Connection: ', conn)

curs = conn.cursor()
print('Cursor: ', curs, '\n')

# Question 1: How many total Characters are there?
query = '''
SELECT
count (distinct character_id)
FROM charactercreator_character;
'''

result = curs.execute(query).fetchall()
print('Question 1: How many total Characters are there?')
print('TOTAL NUMBER OF CHARACTERS: ', result[0][0], '\n')

curs.close()
conn.commit()

# Question 2: How many of each specific subclass?
curs0 = conn.cursor()

query0 = '''
SELECT 'total_avatars' AS class_name
,COUNT (DISTINCT character_id) AS class_count
FROM charactercreator_character c

UNION ALL
SELECT 'mages_NOT_necromancers' AS class_name
,COUNT(DISTINCT m.character_ptr_id) - 
COUNT(DISTINCT n.mage_ptr_id) AS class_count
FROM charactercreator_mage m, charactercreator_necromancer n

UNION ALL
SELECT 'mages_who_ARE_necromancers' AS class_name
,COUNT(DISTINCT n.mage_ptr_id) AS class_count
FROM charactercreator_necromancer n

UNION ALL
SELECT 'thieves' AS class_name
,COUNT (DISTINCT t.character_ptr_id) AS class_count
FROM charactercreator_thief t

UNION ALL
SELECT 'clerics' AS class_name
,COUNT (DISTINCT cl.character_ptr_id) AS class_count
FROM charactercreator_cleric cl

UNION ALL
SELECT 'fighters' AS class_name
,COUNT (DISTINCT f.character_ptr_id) AS class_count
FROM charactercreator_fighter f;
'''

result0 = curs0.execute(query0).fetchall()
df = pd.DataFrame(result0, columns=['subclass_name','class_count'])
print('Question 2: How many of each specific subclass?')
print(df, '\n')

curs0.close()
conn.commit()

# Question 3: How many total Items?
curs1 = conn.cursor()

query1 = '''
SELECT COUNT (DISTINCT ai.item_id) AS total_items
FROM armory_item ai;
'''

result1 = curs1.execute(query1).fetchall()
print('Question 3: How many total Items?')
print(result1[0][0], 'total items \n')

curs1.close()
conn.commit()

# Question 4a: How many of the Items are weapons?
curs2 = conn.cursor()

query2 = '''
SELECT SUM(w.item_ptr_id IS NULL) AS non_weapons
,SUM (w.item_ptr_id IS NOT NULL) AS are_weapons
FROM armory_item ai
LEFT JOIN armory_weapon w
ON ai.item_id = w.item_ptr_id;
'''

result2 = curs2.execute(query2).fetchall()
print('Question 4a: How many of the Items are weapons?')
print(result2[0][1], 'items are weapons \n')

# Question 4b: How many of the Items are NOT weapons?

print('Question 4b: How many of the Items are NOT weapons?')
print(result2[0][0], 'armory items are NOT weapons \n')

curs2.close()
conn.commit()

# Question 5: How many Items does each character have? (Return first 20 rows)?
curs3 = conn.cursor()

query3 = '''
SELECT
c.character_id as pin
,c.name as avatar
,COUNT (inv.item_id) AS item_count
,COUNT (w.item_ptr_id) AS weapon_count
FROM charactercreator_character c
LEFT JOIN charactercreator_character_inventory inv
ON inv.character_id = c.character_id
LEFT JOIN armory_weapon w
ON inv.item_id = w.item_ptr_id
GROUP BY pin
ORDER BY item_count DESC, weapon_count DESC
LIMIT 20;
'''

result3 = curs3.execute(query3).fetchall()
df0 = pd.DataFrame(
    result3,
    columns=['pin','avatar', 'item_count', 'weapon_count']
    )
print(
    'Question 5: How many Items does each character have?',
    ' (Return first 20 rows)'
     )
print(df0, '\n')

curs3.close()
conn.commit()