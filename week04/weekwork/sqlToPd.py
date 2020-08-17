import pandas as pd

person = pd.DataFrame({
    'id':[1,2,3,4,5],
    'order_id':[2,3,4,5,6],
    'name':['Li1','Li2','Li3','Li4','Li5'],
    'age':[10,20,30,40,50]
})

department = pd.DataFrame({
    'id':[1,2,3,4,5],
    'depart':['sale','sale','hr','hr','tech']
})

# 1.  select * from data

print(person[:])
# 2. SELECT * FROM data LIMIT 10

print(person[:10])
# 3. SELECT id FROM data;  //id 是 data 表的特定一列
print(person['id'])
# 4. SELECT COUNT(id) FROM data;
print(person['id'].count())
# 5. SELECT * FROM data WHERE id<1000 AND age>30;

print(person[(person['id']<1000) & (person['age']>30)])
# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
person.groupby('id').aggregate({
    'order_id':pd.Series.nunique
})
# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
print(pd.merge(person,department,how='inner',on='id'))
# 8. SELECT * FROM table1 UNION SELECT * FROM table2;

print(pd.concat([person,department]).drop_duplicates())

# 9. DELETE FROM table1 WHERE id=10;

person.drop(person[person.id == 10].index, axis=0, inplace=True)
# 10. ALTER TABLE table1 DROP COLUMN column_name;

person.drop('id', axis=1, inplace=True)
