
#  Database

###  An interface, using it, can do CRUD operations in MySQL without the need for SQL Query

#
##  Install packages
####  MySQL
```bash
pip install pymysql
```

####  PostgreSQL

```bash
pip install psycopg
```

#
##  Create object
####  MySQL
#####  defult port : 3306
```python
from Database import MySQL


db =  MySQL("localhost",  "root",  "0000",  "test",  3306)
```

####  PostgreSQL
#####  defult port : 5432
```python
from Database import PostgreSQL

db =  PostgreSQL("localhost","root","0000","test",5432)
```

#
#  Let's go!

##  Example table

table name : test

|id|name|phone|
|--|--|--|
|1|Alireza|+989121234567|
|2|Arshia|+989121234568|
|3|Hossein|+989121234569|

#
##  Insert data

```python
table =  "test"
data =  [4,"Arsalan","+989121234560"]
result = db.insert(table,list)
print(result)
```

####  if result is True :
|id|name|phone|
|--|--|--|
|1|Alireza|+989121234567
|2|Arshia|+989121234568
|3|Hossein|+989121234569
|4|Arsalan|+989121234560

#
##  Read data
###  Read a cell
```python
table =  "test"
cell = db.read_cell_by_index(table,1,1)
print(cell)

>>>  "Arshia"
```

###  Read data of a column by column index

```python
table =  "test"
column = db.read_column_by_index(table,1)
print(column)

>>>  ["Alireza","Arshia","Hossein","Arsalan"]
```

###  Read data of a column by column name
```python
table =  "test"
column = db.read_column_by_name(table,"name")
print(column)

>>>  ["Alireza","Arshia","Hossein","Arsalan"]
```

###  Read data of a row by row id
```python
table =  "test"
row = db.read_row_by_id(table,3)
print(row)
  
>>>  [3,"Hossein","+989121234569"]
```

###  Read data of a row by a key
```python
table =  "test"
rows = db.read_rows_by_key(table,"name","Hossein")
print(rows)

>>> ((3,"Hossein","+989121234569"),)
```

* If the functions returns False, there is an error in the args!

#
##  Update data
###  By ID
```python
table =  "test"
result = db.update_cells_by_id(table,4,name="Hossein",phone="+989121234563")
print(result)
```
* if result is True:

|id|name|phone|
|--|--|--|
|1|Alireza|+989121234567
|2|Arshia|+989121234568
|3|Hossein|+989121234569
|4|Hossein|+989121234563

###  By a Key
```python
table =  "test"
result = db.update_cells_by_key(table,"name","Hossein",name="Amir", phone="+989121234565")
print(result)
```
* if result is True:

|id|name|phone|
|--|--|--|
|1|Alireza|+989121234567
|2|Arshia|+989121234568
|3|Amir|+989121234565
|4|Amir|+989121234565

#

##  Delete data
###  By ID
```python
table =  "test"
result = db.delete_row_by_id(table,2)
print(result)
```
* if result is True:

|id|name|phone|
|--|--|--|
|1|Alireza|+989121234567
|3|Hossein|+989121234569
|4|Hossein|+989121234563

###  By a Key
```python
table =  "test"
result = db.delete_rows_by_key(table,"name","Amir")
print(result)
```
* if result is True:

|id|name|phone|
|--|--|--|
|1|Alireza|+989121234567
||