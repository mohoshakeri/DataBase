# Get Started

```bash
 pip install pymysql
 pip install psycopg
```

#### Create DataBase in MySQL

#### Create a Table

```python
from DataBase import MySQL
from DataBase import PostgreSQL

#Object
db = MySQL(host="127.0.0.1", user="root", passwd="", port=4306, db="test")
db = PostgreSQL(host="127.0.0.1", user="root", passwd="", port=4306, db="test")


#Insert
db.insert("TableName", "Value-1", "Value-2", "Value-3")  # And ...

#Read
db.read("TableName")#Read all Values
db.readAColumn("TableName",2)#Read third column
db.readByIndex("TableName", 1, 1) #Enter index of table ex: [1][2]
db.readFromID("TableName", "IdNumber") #Create a column in mysql named id
db.readFromAValue("TableName", "Column", "ColumnValue") #without id


db.updateACellByID(
    "TableName", "UpdateColumn", "UpdateValue", "Id"
    )#Create a column in mysql named id

db.updateACellByValue(
    "TableName", "UpdateColumn", "UpdateValue", "IdColumn", "IdColumnValue"
)#without id

db.updateCellsByID(
    "TableName", "Id", UpdateColumn_1="UpdateValue-1", UpdateColumn_2="UpdateValue-2"
)  # And ... #Create a column in mysql named id

db.updateCellsByValue(
    "TableName",
    "IdColumn",
    "IdColumnValue",
    UpdateColumn_1="UpdateValue-1",
    UpdateColumn_2="UpdateValue-2",
) # And ... #without id

db.deleteCellByID("TableName", "4") #Create a column in mysql named id
db.deleteCellByValue("TableName", "name", "Ali") #without id

db.clear("TableName")
```

### if the functions return False amount ie there is a problem in SQL commands.
