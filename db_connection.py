"""
Data Base Connection File
"""

import os
import pandas as pd
from sqlalchemy import create_engine
import sqlite3
import redshift_connector
from dotenv import load_dotenv
load_dotenv()


class DatabaseConnection:

    def __init__(self, db_type: str):
        self.db_type = db_type

    def connect(self):
        """
        Connect to the database and return the connection object
        Args:
            None
        Returns:
            self.conn: Connection object
        """
        if self.db_type == "sqllite":
            db_path = "student.db"
            self.connection = sqlite3.connect(db_path)
            return self.connection
        elif self.db_type == "postgresql":
            DATABASE_USERNAME = os.getenv("DB_USER")
            DATABASE_PASSWORD = os.getenv("DB_PASSWORD")
            DATABASE_HOST = os.getenv("DB_HOST")
            DATABASE_PORT = os.getenv("DB_PORT")
            DATABASE_NAME = os.getenv("DB_NAME")
            self.connection = redshift_connector.connect(
                host=DATABASE_HOST,
                database=DATABASE_NAME,
                user=DATABASE_USERNAME,
                password=DATABASE_PASSWORD,
                port=DATABASE_PORT
            )
            return self.connection
        else:
            raise Exception(f"Invalid database type: {self.db_type}")

    def execute_query(self, query):
        """
        Execute a query and return the result as a pandas dataframe
        Args:
            query: SQL query to execute
        Returns:
            df: pandas dataframe
        """
        if not self.connection:
            self.connect()

        if self.db_type == "sqllite":
            df = pd.read_sql_query(query, self.connection)
        elif self.db_type == "postgresql":
            df = pd.read_sql_query(query, self.connection)
        else:
            raise Exception(f"Invalid database type: {self.db_type}")
        return df
 

    def get_schema_info(self) -> str:
        """
        Get the schema information for a given table
        Args:
            schema_name: name of the schema
            table_name: name of the table
        Returns:
            schema_info: list of schema information
        """
        schema_info = []
        if self.db_type == "sqllite":
            cursor = self.connection.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()

            for table in tables:
                table_name = table[0]
                cursor.execute(f"PRAGMA table_info({table_name});")
                columns = cursor.fetchall()
                col_info = ", ".join([f"{col[1]}: {col[2]}" for col in columns])
                schema_info.append(f"Table: {table_name}\nColumns: {col_info}\n")

        elif self.db_type == "postgresql":
            query = f"""
            SELECT table_schema, table_name, column_name, data_type 
            FROM information_schema.columns 
            WHERE table_schema = 'legacy_dm' and table_name = 'fact_live_product_sales'
            ORDER BY table_name, ordinal_position
            LIMIT 100
            """
            df = pd.read_sql_query(query, self.connection)
            for table in df['table_name'].unique():
                cols = df[df['table_name'] ==  table]
                table_schema = cols.iloc[0]['table_schema']
                col_info = ", ".join([f"{col['column_name']}: {col['data_type']}" for _, col in cols.iterrows()])
                schema_info.append(f"Table: {table_schema}.{table}\nColumns: {col_info}\n")
        print(schema_info)
        return "\n".join(schema_info)

    def close(self):
        if self.connection:
            if self.db_type == "sqllite":
                self.connection.close()
            elif self.db_type == "postgresql":
                self.connection.close()
            self.connection = None
