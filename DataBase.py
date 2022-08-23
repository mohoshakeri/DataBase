import psycopg
import pymysql


class MySQL:
    def __init__(self, host, user, passwd, port, db):
        global mydb
        mydb = pymysql.connect(
            port=port, host=host, user=user, passwd=passwd, database=db
        )
        global cursor
        cursor = mydb.cursor()

    def clear(self, table):
        clear = f"TRUNCATE {table};"
        try:
            res = cursor.execute(clear)
            mydb.commit()
            return True if res == 1 else False
        except:
            return False

    def insert(self, table, *values):
        insert = f"INSERT INTO {table} VALUES {values};"
        try:
            res = cursor.execute(insert)
            mydb.commit()
            return True if res == 1 else False
        except:
            return False

    def read(self, table):
        read = f"SELECT * FROM {table};"
        try:
            cursor.execute(read)
            x = cursor.fetchall()
            return x
        except:
            return False

    def readAColumn(self, table, columnindex):
        columnList = self.read(table)
        if columnList == False:
            return False
        else:
            result = []
            for item in columnList:
                result.append(item[columnindex])
            return result

    def readByIndex(self, table, index1, index2):
        read = f"SELECT * FROM {table};"
        try:
            cursor.execute(read)
            x = cursor.fetchall()
            return x[index1][index2]
        except:
            return False

    def readFromID(self, table, id):
        read = f"SELECT * FROM {table} WHERE {table}.id = '{id}';"
        try:
            cursor.execute(read)
            x = cursor.fetchall()
            return x[0]
        except:
            return False

    def readFromAValue(self, table, columnName, columnValue):
        read = f"SELECT * FROM {table} WHERE {table}.{columnName} = '{columnValue}';"
        try:
            cursor.execute(read)
            x = cursor.fetchall()
            return x
        except:
            return False

    def updateACellByID(self, table, columnName, value, id):
        update = (
            f"UPDATE {table} SET {columnName} = '{value}' WHERE {table}.id = '{id}';"
        )
        try:
            res = cursor.execute(update)
            mydb.commit()
            return True if res == 1 else False
        except:
            return False

    def updateACellByValue(self, table, columnName, value, IDcolumnName, idValue):
        update = f"UPDATE {table} SET {columnName} = '{value}' WHERE {table}.{IDcolumnName} = '{idValue}';"
        try:
            res = cursor.execute(update)
            mydb.commit()
            return True if res == 1 else False
        except:
            return False

    def updateCellsByID(self, table, id, **columnsValues):
        result = []
        columns = list(columnsValues.keys())
        values = list(columnsValues.values())
        for index in range(len(columns)):
            try:
                res = self.updateACellByID(table, columns[index], values[index], id)
                mydb.commit()
                result.append(True) if res else result.append(True)
            except:
                result = result.append(False)
        return True in result

    def updateCellsByValue(self, table, IDcolumnName, idValue, **columnsValues):
        result = []
        columns = list(columnsValues.keys())
        values = list(columnsValues.values())
        for index in range(len(columns)):
            try:
                res = self.updateACellByValue(
                    table, columns[index], values[index], IDcolumnName, idValue
                )
                mydb.commit()
                result.append(True) if res else result.append(True)
            except:
                result = result.append(False)
        return True in result

    def deleteCellByID(self, table, id):
        delete = f"DELETE FROM {table} WHERE {table}.id='{id}';"
        try:
            res = cursor.execute(delete)
            mydb.commit()
            return True if res == 1 else False
        except:
            return False

    def deleteCellByValue(self, table, IDcolumnName, idValue):
        delete = f"DELETE FROM {table} WHERE {table}.{IDcolumnName}='{idValue}';"
        try:
            res = cursor.execute(delete)
            mydb.commit()
            return True if res else False
        except:
            return False

    def close():
        mydb.close()


class PostgreSQL:
    def __init__(self, host, user, passwd, port, db):
        global mydb
        mydb = psycopg.connect(
            port=port, host=host, user=user, password=passwd, dbname=db
        )
        global cursor
        cursor = mydb.cursor()

    def clear(self, table):
        clear = f"TRUNCATE {table};"
        try:
            res = cursor.execute(clear)
            mydb.commit()
            return True if res == 1 else False
        except:
            return False

    def insert(self, table, *values):
        insert = f"INSERT INTO {table} VALUES {values};"
        try:
            res = cursor.execute(insert)
            mydb.commit()
            return True if res == 1 else False
        except:
            return False

    def read(self, table):
        read = f"SELECT * FROM {table};"
        try:
            cursor.execute(read)
            x = cursor.fetchall()
            return x
        except:
            return False

    def readAColumn(self, table, columnindex):
        columnList = self.read(table)
        if columnList == False:
            return False
        else:
            result = []
            for item in columnList:
                result.append(item[columnindex])
            return result

    def readByIndex(self, table, index1, index2):
        read = f"SELECT * FROM {table};"
        try:
            cursor.execute(read)
            x = cursor.fetchall()
            return x[index1][index2]
        except:
            return False

    def readFromID(self, table, id):
        read = f"SELECT * FROM {table} WHERE {table}.id = '{id}';"
        try:
            cursor.execute(read)
            x = cursor.fetchall()
            return x[0]
        except:
            return False

    def readFromAValue(self, table, columnName, columnValue):
        read = f"SELECT * FROM {table} WHERE {table}.{columnName} = '{columnValue}';"
        try:
            cursor.execute(read)
            x = cursor.fetchall()
            return x
        except:
            return False

    def updateACellByID(self, table, columnName, value, id):
        update = (
            f"UPDATE {table} SET {columnName} = '{value}' WHERE {table}.id = '{id}';"
        )
        try:
            res = cursor.execute(update)
            mydb.commit()
            return True if res == 1 else False
        except:
            return False

    def updateACellByValue(self, table, columnName, value, IDcolumnName, idValue):
        update = f"UPDATE {table} SET {columnName} = '{value}' WHERE {table}.{IDcolumnName} = '{idValue}';"
        try:
            res = cursor.execute(update)
            mydb.commit()
            return True if res == 1 else False
        except:
            return False

    def updateCellsByID(self, table, id, **columnsValues):
        result = []
        columns = list(columnsValues.keys())
        values = list(columnsValues.values())
        for index in range(len(columns)):
            try:
                res = self.updateACellByID(table, columns[index], values[index], id)
                mydb.commit()
                result.append(True) if res else result.append(True)
            except:
                result = result.append(False)
        return True in result

    def updateCellsByValue(self, table, IDcolumnName, idValue, **columnsValues):
        result = []
        columns = list(columnsValues.keys())
        values = list(columnsValues.values())
        for index in range(len(columns)):
            try:
                res = self.updateACellByValue(
                    table, columns[index], values[index], IDcolumnName, idValue
                )
                mydb.commit()
                result.append(True) if res else result.append(True)
            except:
                result = result.append(False)
        return True in result

    def deleteCellByID(self, table, id):
        delete = f"DELETE FROM {table} WHERE {table}.id='{id}';"
        try:
            res = cursor.execute(delete)
            mydb.commit()
            return True if res == 1 else False
        except:
            return False

    def deleteCellByValue(self, table, IDcolumnName, idValue):
        delete = f"DELETE FROM {table} WHERE {table}.{IDcolumnName}='{idValue}';"
        try:
            res = cursor.execute(delete)
            mydb.commit()
            return True if res else False
        except:
            return False

    def close():
        mydb.close()
