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
FROM Employee;
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
GROUP BY City;
'''

town_age = curs0.execute(q1).fetchall()
print('(Stretch) How does the average age of employee at hire vary by city?')
print(town_age)
ages = []
for tup in town_age:
    ages.append(tup[1])
print(f'The average employee age in each city range from {int(min(ages))}',
f'to {int(max(ages))} \n')

# What are the ten most expensive items (per unit price) in the database and 
# their suppliers?

q2 = '''
SELECT 
p.ProductName,
p.UnitPrice,
s.CompanyName
FROM Product p
LEFT JOIN Supplier s
ON s.Id = p.SupplierId
ORDER BY UnitPrice DESC
LIMIT 10;
'''

supply = curs0.execute(q2).fetchall()
print('What are the ten most expensive items (per unit price) in the',
' database and their suppliers?')
for x in range(len(supply)):
    print(f'{supply[x][0]}, ${supply[x][1]}, supplier: {supply[x][2]}')
print('\n')

# What is the largest category (by number of unique products in it)?

q3 = '''
SELECT 
g.CategoryName,
COUNT (*) AS unq_prod
FROM Product p
LEFT JOIN Category g
ON g.Id = p.CategoryId
GROUP BY g.Id
ORDER BY unq_prod DESC;
'''

catg = curs0.execute(q3).fetchall()
print('What is the largest category (by number of unique products in it)?')
for x in range(len(catg)):
    print(f'{catg[x][0]}, category: {catg[x][1]}')
print(f'With {catg[0][1]} distinct products, {catg[0][0]} is the category',
' with the most number of unique products. \n')

# (Stretch) Who's the employee with the most territories? Use TerritoryId 
# (not name, region, or other fields) as the unique identifier for
# territories.

q4 = '''
SELECT
e.FirstName,
e.LastName,
COUNT (*) as turfs
FROM EmployeeTerritory t
LEFT JOIN Employee e
ON e.Id = t.EmployeeId
GROUP BY e.FirstName
ORDER BY turfs DESC;
'''

turf = curs0.execute(q4).fetchone()
print(f'{turf[0]} {turf[1]} manages {turf[2]} territories, more than any',
'other employee. \n')

curs0.close()
conn0.commit()