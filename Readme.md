# Get Started

## 1- install packages

```bash
 pip install pymysql
 pip install psycopg
```

### 2- Create DataBase in MySQL or PostgreSQL

### 3- Create a Table

### 4- Use Classes

## TIP: if the functions return False amount ie there is a problem in SQL commands.

```python
from DataBase import MySQL
from DataBase import PostgreSQL

#Object
db = MySQL(host="127.0.0.1", user="root", passwd="", port=4306, db="test")
db = PostgreSQL(host="127.0.0.1", user="root", passwd="", port=4306, db="test")


#Insert
db.insert("TableName", "Value-1", "Value-2", "Value-3")  # And ...

#Read
db.read("TableName")# Return a touple contains all values
db.readAColumn("TableName",2)# Return a list contains third column values
db.readByIndex("TableName", 1, 2) # Return Value [1][2]

# First create a column named id
db.readFromID("TableName", "IdNumber") # Return a touple contains IDNumber value
db.readFromAValue("TableName", "Column", "ColumnValue") # Return a touple contains ColumnValue


db.updateACellByID(
    "TableName", "UpdateColumn", "UpdateValue", "Id"
    )#Update a cell by id

db.updateACellByValue(
    "TableName", "UpdateColumn", "UpdateValue", "IdColumn", "IdColumnValue"
)#without id

db.updateCellsByID(
    "TableName", "Id", UpdateColumn_1="UpdateValue-1", UpdateColumn_2="UpdateValue-2"
)  #Update some cells by id

db.updateCellsByValue(
    "TableName",
    "IdColumn",
    "IdColumnValue",
    UpdateColumn_1="UpdateValue-1",
    UpdateColumn_2="UpdateValue-2",
) #without id

db.deleteCellByID("TableName", "IDNumber") # Drop a cell contains IDNumber
db.deleteCellByValue("TableName", "Column", "ColumnValue") #without id

db.clear("TableName")
```
