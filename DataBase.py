from typing import Iterable
import psycopg
import pymysql


class MySQL:
    """An ORM, using it, can do CRUD operations in MySQL without the need for SQL Query

    Args:
        host (str): MySQL Server host Ex localhost
        user (str): MySQL account user name Ex root
        passwd (str): MySQL account user password Ex 0000
        db (str): MySQL database name
        port (int) [optional]: MySQL Server port (default = 3306)
    """

    def __init__(self, host: str, user: str, passwd: str, db: str, port: int = 3306):
        self._mydb = pymysql.connect(
            port=port, host=host, user=user, passwd=passwd, database=db
        )
        self._cursor = self._mydb.cursor()

    def id_validation(self, id):
        try:
            id = int(id)
            return id
        except TypeError:
            raise TypeError("id must be a number")
        except ValueError:
            raise TypeError("id must be a number")

    def clear(self, table: str):
        """Clear all data from a table

        Args:
            table (str): a table name
        Returns:
            True: if commands are properly executed
            False: if an error occurs
        """
        clear = f"TRUNCATE {table};"
        try:
            action = self._cursor.execute(clear)
            self._mydb.commit()
            return True if action == 1 else False
        except:
            return False

    def insert(self, table: str, values: Iterable):
        """Insert values to a table

        Args:
            table (str): a table name
            values (Iterable): values for insert
                TIP:
                    if you don't enter required values (NULL = False)
                    or type of value is wrong,
                    the function returns False
        Returns:
            True: if commands are properly executed
            False: if an error occurs
        """
        insert = f"INSERT INTO {table} VALUES {tuple(values)};"
        try:
            action = self._cursor.execute(insert)
            self._mydb.commit()
            return True if action == 1 else False
        except:
            return False

    def read(self, table: str):
        """Read all data of a table

        Args:
            table (str): a table name
        Returns:
            Tuple contains all rows to type tuple
            False: if an error occurs
        """
        read = f"SELECT * FROM {table};"
        try:
            self._cursor.execute(read)
            result = self._cursor.fetchall()
            return result
        except:
            return False

    def read_column_by_name(self, table: str, column_name: str):
        """Read data of column from a table by column name

        Args:
            table (str): a table name
            column_name (str): a column name
        Returns:
            List contains column data
            False: if an error occurs
        """
        read = f"SELECT {column_name} FROM {table}"
        try:
            self._cursor.execute(read)
            data = self._cursor.fetchall()
            result = []
            for tuple in data:
                result.append(tuple[0])
            return result
        except:
            return False

    def read_column_by_index(self, table: str, column_index: int):
        """Read data of column from a table by column index

        Args:
            table (str): a table name
            column_index (int): a column index
        Returns:
            List contains column data
            False: if an error occurs
        """
        try:
            column_index = int(column_index)
        except TypeError:
            raise TypeError("column_index must be a Integer")
        except ValueError:
            raise TypeError("column_index must be a Integer")

        column_list = self.read(table)
        if column_list == False:
            return False
        else:
            result = []
            for item in column_list:
                result.append(item[column_index])
            return result

    def read_cell_by_index(self, table: str, row: int, column: int):
        """Get a cell of a table by its index

        Args:
            table (str): a table name
            row (int): row index
            column (int): column index
        Returns:
            Value of cell
            False: if an error occurs
        """
        try:
            row = int(row)
            column = int(column)
        except TypeError:
            raise TypeError("index must be a Integer")
        except ValueError:
            raise TypeError("index must be a Integer")

        read = f"SELECT * FROM {table};"
        try:
            self._cursor.execute(read)
            result = self._cursor.fetchall()
            return result[row][column]
        except:
            return False

    def read_row_by_id(self, table: str, id: int | str):
        """Get a row data of a table by id

        Args:
            table (str): a table name
            id (int | str): id of row (primary_key)
        Returns:
            List: contains row data
            False : if an error occurs
        """
        id = self.id_validation(id)
        read = f"SELECT * FROM {table} WHERE {table}.id = '{id}';"
        try:
            self._cursor.execute(read)
            data = self._cursor.fetchall()
            return data[0]
        except:
            return False

    def read_rows_by_key(self, table: str, column_name: str, key: str):
        """Get some rows data of a table by a key

        Args:
            table (str): a table name
            column_name (str): a column contains key
            key (str): key for search rows

        Returns:
            Tuple: contains rows to type tuple
            False : if an error occurs
        """
        read = f"SELECT * FROM {table} WHERE {table}.{column_name} = '{key}';"
        try:
            self._cursor.execute(read)
            result = self._cursor.fetchall()
            return result
        except:
            return False

    def _update_cell_by_id(self, table: str, column_name: str, value, id: str | int):
        """Internal function

        Update a cell of a table by its row id
        """
        id = self.id_validation(id)
        update = (
            f"UPDATE {table} SET {column_name} = '{value}' WHERE {table}.id = '{id}';"
        )
        try:
            action = self._cursor.execute(update)
            self._mydb.commit()
            return True if action == 1 else False
        except:
            return False

    def _update_cell_by_key(
        self, table: str, key_column_name: str, key: str, column_name: str, value: str
    ):
        """Internal function

        Update some cells of a table by a key
        """
        update = f"UPDATE {table} SET {column_name} = '{value}' WHERE {table}.{key_column_name} = '{key}';"
        try:
            action = self._cursor.execute(update)
            self._mydb.commit()
            return True if action == 1 else False
        except:
            return False

    def update_cells_by_id(self, table: str, id: int, **values):
        """Update some cells of a table by row id

        Args:
            table (str): a table name
            id (str | int): id of row (primary_key)
            values (any): some value that will replaced [column_name = value]
                TIP: if type of value is wrong,
                the function returns False
                Ex: username="John",password="1234"

        Returns:
            True: if commands are properly executed
            False: if an error occurs
        """
        id = self.id_validation(id)
        result = []
        columns = list(values.keys())
        values = list(values.values())
        for index in range(len(columns)):
            try:
                action = self._update_cell_by_id(
                    table, columns[index], values[index], id
                )
                self._mydb.commit()
                result.append(True) if action else result.append(False)
            except:
                result.append(False)
        return True in result

    def update_cells_by_key(self, table, key_column_name, key, **values):
        """Update some cells of a table by a key

        Args:
            table (str): a table name
            key_column_name (str): a column contains key
            key (str): key for search row
            values (any): some value that will replaced [column_name = value]
                TIP: if type of value is wrong,
                the function returns False
                Ex: username="John",password="1234"

        Returns:
            True: if commands are properly executed
            False: if an error occurs
        """
        result = []
        columns = list(values.keys())
        values = list(values.values())
        for index in range(len(columns)):
            try:
                action = self._update_cell_by_key(
                    table, key_column_name, key, columns[index], values[index]
                )
                self._mydb.commit()
                result.append(True) if action else result.append(False)
            except:
                result.append(False)
        return True in result

    def delete_row_by_id(self, table: str, id: int):
        """Delete a row of a table by its row id

        Args:
            table (str): a table name
            id (str | int): id of row (primary_key)

        Returns:
            True: if commands are properly executed
            False: if an error occurs
        """
        id = self.id_validation(id)
        delete = f"DELETE FROM {table} WHERE {table}.id='{id}';"
        try:
            action = self._cursor.execute(delete)
            self._mydb.commit()
            return True if action == 1 else False
        except:
            return False

    def delete_rows_by_key(self, table: str, key_column_name: str, key: str):
        """Delete some rows of a table by a key

        Args:
            table (str): a table name
            key_column_name (str): a column contains key
            key (str): key for search row

        Returns:
            True: if commands are properly executed
            False: if an error occurs
        """
        delete = f"DELETE FROM {table} WHERE {table}.{key_column_name}='{key}';"
        try:
            action = self._cursor.execute(delete)
            self._mydb.commit()
            return True if action else False
        except:
            return False

    def close(self):
        """Close database"""
        self._mydb.close()


class PostgreSQL:
    """
    An ORM, using it, can do CRUD operations in PostgreSQL without the need for SQL Query

    Args:
        host (str): PostgreSQL Server host Ex 'localhost'
        user (str): PostgreSQL account user name Ex 'root'
        passwd (str): PostgreSQL account user password Ex '0000'
        db (str): PostgreSQL database name
        port (int) [optional]: PostgreSQL Server port (default = 5432)
    """

    def __init__(self, host: str, user: str, passwd: str, db: str, port: int = 5432):
        self._mydb = psycopg.connect(
            port=port, host=host, user=user, password=passwd, dbname=db
        )
        self._cursor = self._mydb.cursor()

    def id_validation(self, id):
        try:
            id = int(id)
            return id
        except TypeError:
            raise TypeError("id must be a number")
        except ValueError:
            raise TypeError("id must be a number")

    def clear(self, table: str):
        """Clear all data from a table

        Args:
            table (str): a table name
        Returns:
            True: if commands are properly executed
            False: if an error occurs
        """
        clear = f"TRUNCATE {table};"
        try:
            action = self._cursor.execute(clear)
            self._mydb.commit()
            return True if "COMMAND_OK" in str(action) else False
        except:
            return False

    def insert(self, table: str, values: Iterable):
        """Insert values to a table

        Args:
            table (str): a table name
            values (Iterable): values for insert
                TIP:
                    if you don't enter required values (NULL = False)
                    or type of value is wrong,
                    the function returns False
        Returns:
            True: if commands are properly executed
            False: if an error occurs
        """
        insert = f"INSERT INTO {table} VALUES {tuple(values)};"
        try:
            action = self._cursor.execute(insert)
            self._mydb.commit()
            return True if "COMMAND_OK" in str(action) else False
        except:
            return False

    def read(self, table: str):
        """Read all data of a table

        Args:
            table (str): a table name
        Returns:
            Tuple contains all rows to type tuple
            False: if an error occurs
        """
        read = f"SELECT * FROM {table};"
        try:
            self._cursor.execute(read)
            result = self._cursor.fetchall()
            return result
        except:
            return False

    def read_column_by_name(self, table: str, column_name: str):
        """Read data of column from a table by column name

        Args:
            table (str): a table name
            column_name (str): a column name
        Returns:
            List contains column data
            False: if an error occurs
        """
        read = f"SELECT {column_name} FROM {table}"
        try:
            self._cursor.execute(read)
            data = self._cursor.fetchall()
            result = []
            for tuple in data:
                result.append(tuple[0])
            return result
        except:
            return False

    def read_column_by_index(self, table: str, column_index: int):
        """Read data of column from a table by column index

        Args:
            table (str): a table name
            column_index (int): a column index
        Returns:
            List contains column data
            False: if an error occurs
        """
        try:
            column_index = int(column_index)
        except TypeError:
            raise TypeError("column_index must be a Integer")
        except ValueError:
            raise TypeError("column_index must be a Integer")

        column_list = self.read(table)
        if column_list == False:
            return False
        else:
            result = []
            for item in column_list:
                result.append(item[column_index])
            return result

    def read_cell_by_index(self, table: str, row: int, column: int):
        """Get a cell of a table by its index

        Args:
            table (str): a table name
            row (int): row index
            column (int): column index
        Returns:
            Value of cell
            False: if an error occurs
        """
        try:
            row = int(row)
            column = int(column)
        except TypeError:
            raise TypeError("index must be a Integer")
        except ValueError:
            raise TypeError("index must be a Integer")

        read = f"SELECT * FROM {table};"
        try:
            self._cursor.execute(read)
            result = self._cursor.fetchall()
            return result[row][column]
        except:
            return False

    def read_row_by_id(self, table: str, id: int | str):
        """Get a row data of a table by id

        Args:
            table (str): a table name
            id (int | str): id of row (primary_key)
        Returns:
            List: contains row data
            False : if an error occurs
        """
        id = self.id_validation(id)
        read = f"SELECT * FROM {table} WHERE {table}.id = '{id}';"
        try:
            self._cursor.execute(read)
            data = self._cursor.fetchall()
            return data[0]
        except:
            return False

    def read_rows_by_key(self, table: str, column_name: str, key: str):
        """Get some rows data of a table by a key

        Args:
            table (str): a table name
            column_name (str): a column contains key
            key (str): key for search rows

        Returns:
            Tuple: contains rows to type tuple
            False : if an error occurs
        """
        read = f"SELECT * FROM {table} WHERE {table}.{column_name} = '{key}';"
        try:
            self._cursor.execute(read)
            result = self._cursor.fetchall()
            return result
        except:
            return False

    def _update_cell_by_id(self, table: str, column_name: str, value, id: str | int):
        """Internal function

        Update a cell of a table by its row id
        """
        id = self.id_validation(id)
        update = (
            f"UPDATE {table} SET {column_name} = '{value}' WHERE {table}.id = '{id}';"
        )
        try:
            action = self._cursor.execute(update)
            self._mydb.commit()
            return True if "COMMAND_OK" in str(action) else False
        except:
            return False

    def _update_cell_by_key(
        self, table: str, key_column_name: str, key: str, column_name: str, value: str
    ):
        """Internal function

        Update some cells of a table by a key
        """
        update = f"UPDATE {table} SET {column_name} = '{value}' WHERE {table}.{key_column_name} = '{key}';"
        try:
            action = self._cursor.execute(update)
            self._mydb.commit()
            return True if "COMMAND_OK" in str(action) else False
        except:
            return False

    def update_cells_by_id(self, table: str, id: int, **values):
        """Update some cells of a table by row id

        Args:
            table (str): a table name
            id (str | int): id of row (primary_key)
            values (any): some value that will replaced [column_name = value]
                TIP: if type of value is wrong,
                the function returns False
                Ex: username="John",password="1234"

        Returns:
            True: if commands are properly executed
            False: if an error occurs
        """
        id = self.id_validation(id)
        result = []
        columns = list(values.keys())
        values = list(values.values())
        for index in range(len(columns)):
            try:
                action = self._update_cell_by_id(
                    table, columns[index], values[index], id
                )
                self._mydb.commit()
                result.append(True) if action else result.append(False)
            except:
                result.append(False)
        return True in result

    def update_cells_by_key(self, table, key_column_name, key, **values):
        """Update some cells of a table by a key

        Args:
            table (str): a table name
            key_column_name (str): a column contains key
            key (str): key for search row
            values (any): some value that will replaced [column_name = value]
                TIP: if type of value is wrong,
                the function returns False
                Ex: username="John",password="1234"

        Returns:
            True: if commands are properly executed
            False: if an error occurs
        """
        result = []
        columns = list(values.keys())
        values = list(values.values())
        for index in range(len(columns)):
            try:
                action = self._update_cell_by_key(
                    table, key_column_name, key, columns[index], values[index]
                )
                self._mydb.commit()
                result.append(True) if action else result.append(False)
            except:
                result.append(False)
        return True in result

    def delete_row_by_id(self, table: str, id: int):
        """Delete a row of a table by its row id

        Args:
            table (str): a table name
            id (str | int): id of row (primary_key)

        Returns:
            True: if commands are properly executed
            False: if an error occurs
        """
        id = self.id_validation(id)
        delete = f"DELETE FROM {table} WHERE {table}.id='{id}';"
        try:
            action = self._cursor.execute(delete)
            self._mydb.commit()
            return True if "COMMAND_OK" in str(action) else False
        except:
            return False

    def delete_rows_by_key(self, table: str, key_column_name: str, key: str):
        """Delete some rows of a table by a key

        Args:
            table (str): a table name
            key_column_name (str): a column contains key
            key (str): key for search row

        Returns:
            True: if commands are properly executed
            False: if an error occurs
        """
        delete = f"DELETE FROM {table} WHERE {table}.{key_column_name}='{key}';"
        try:
            action = self._cursor.execute(delete)
            self._mydb.commit()
            return True if "COMMAND_OK" in str(action) else False
        except:
            return False

    def close(self):
        """Close database"""
        self._mydb.close()
