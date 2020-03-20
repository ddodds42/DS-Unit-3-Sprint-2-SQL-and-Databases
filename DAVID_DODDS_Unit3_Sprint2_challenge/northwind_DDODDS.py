import sqlite3

conn0 = sqlite3.connect('northwind_small.sqlite3')
curs0 = conn0.cursor()

# What are the ten most expensive items (per unit price) in the database?

quer = '''
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
'''

pricey = curs0.execute(quer).fetchall()
print('\n', 'What are the ten most expensive items (per unit price) in the',
' database?')
for x in range(10):
    print(f'{pricey[x][0]}, ${pricey[x][1]}')
print('\n')

# What is the average age of an employee at the time of their hiring? (Hint: 
# a lot of arithmetic works with dates.)

q0 = '''
SELECT
AVG (HireDate - BirthDate) AS avg_age
FROM Employee
'''

age = curs0.execute(q0).fetchone()
print('What is the average age of an employee at the time of their hiring?')
print(f'The average age of a fresh hire is {int(age[0])} years old. \n')

# (Stretch) How does the average age of employee at hire vary by city?

q1 = '''
SELECT 
City,
AVG (HireDate - BirthDate) AS avg_age
FROM Employee
GROUP BY City
'''

town_age = curs0.execute(q1).fetchall()
print('(Stretch) How does the average age of employee at hire vary by city?')
print(town_age)
ages = []
for tup in town_age:
    ages.append(tup[1])
print(f'The average employee age in each city range from {int(min(ages))}',
f'to {int(max(ages))} \n')

curs0.close()
conn0.commit()