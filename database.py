import sqlite3 as sql
import sys

class DB:
    cur = None
    con = None

    def __init__(self, db_name):
        try:
            self.con = sql.connect(db_name, check_same_thread=False)
            self.cur = self.con.cursor()
            self.cur.execute("PRAGMA foreign_keys=ON;")
        except sql.Error:
            print("Error")
            sys.exit(1)

    def __del__(self):
        if self.con:
            print("Closing connection to the db")
            self.con.close()

    def view_all(self, table_name):
        all_data = self.cur.execute(f'SELECT * FROM {table_name}')
        return all_data.fetchall()

    def insert(self, table_name, vals):
        separator = ","
        col_names = separator.join(vals.keys())
        wrapped_val = map(lambda x: f'"{x}"', vals.values())
        values = separator.join(list(wrapped_val))
        sql_statement = f'INSERT INTO {table_name}({col_names}) VALUES({values})'
        self.cur.execute(sql_statement)
        self.con.commit()

    def modify(self, table_name, changes, conditions):
        sql_statement = f'UPDATE {table_name} SET {changes} WHERE {conditions}'
        self.cur.execute(sql_statement)
        self.con.commit()
    
    def delete(self, table_name, conditions):
        sql_statement = f'DELETE FROM {table_name} WHERE {conditions}'
        self.cur.execute(sql_statement)
        self.con.commit()
    
