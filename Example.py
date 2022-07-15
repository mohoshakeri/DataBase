from DataBase import MySQL

db = MySQL(host="127.0.0.1", user="root", passwd="", port=4306, db="test")  # object

db.insert("TableName", "Value-1", "Value-2", "Value-3")  # And ...

db.readByIndex("TableName", 1, 1)
db.readFromID("TableName", "IdNumber")
db.readFromAValue("TableName", "Column", "ColumnValue")

db.updateACellByID("TableName", "UpdateColumn", "UpdateValue", "Id")
db.updateACellByValue(
    "TableName", "UpdateColumn", "UpdateValue", "IdColumn", "IdColumnValue"
)
db.updateCellsByID(
    "TableName", "Id", UpdateColumn_1="UpdateValue-1", UpdateColumn_2="UpdateValue-2"
)  # And ...
db.updateCellsByValue(
    "TableName",
    "IdColumn",
    "IdColumnValue",
    UpdateColumn_1="UpdateValue-1",
    UpdateColumn_2="UpdateValue-2",
)

db.deleteCellByID("TableName", "4")
db.deleteCellByValue("TableName", "name", "Ali")

db.clear("TableName")
