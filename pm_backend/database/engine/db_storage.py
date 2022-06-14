#!/usr/bin/python3
"""Contains:
    (class) DBStorage.
"""
from sqlite3 import Cursor
import mysql.connector


class DBStorage:
    """Class that interacts with the MySQL database.
    """
    __cursor = None
    __connector = None

    def __init__(self):
        """Initialize a new instance of the class.
        """
        self.__connector = mysql.connector.connect(
                                    user='development',
                                    password='dev_pwd(001)',
                                    host='127.0.0.1',
                                    database='project_management')

        self.__connector.autocommit = False

    def open_db(self):
        """Open the connection to the MySQL Database.
        """
        try:
            self.__cursor = self.__connector.cursor(dictionary=True)
            print("Connection is open")
        except mysql.connector.Error as error:
            print(error)

    def close_db(self):
        """Close the connection to the MySQL Database.
        """
        if self.__connector.is_connected():
            self.__cursor.close()
            self.__connector.close()
            print("Connection is closed")

    def exec_procedure(self, name, parameters=[]):
        """Execute a stored procedure on the MySQL Database.

        Args:
            name (str): Stored procedure name.
            parameters (list): Sorted parameter list.

        Returns:
            list: Return the result of the procedure.
        """
        try:
            records = []
            self.__cursor.callproc(name, parameters)
            for result in self.__cursor.stored_results():
                data = result.fetchall()
                if data:
                    records.append(data)
            self.__connector.commit()
            return (records)
        except mysql.connector.Error as error:
            self.__connector.rollback()
            print(error)

    def exec_save(self, name, parameters=[]):
        """Execute a stored procedure on the MySQL Database.

        Args:
            name (str): Stored procedure name.
            parameters (list): Sorted parameter list.

        Returns:
            bool: True or False.
        """
        is_correct = False
        try:
            self.__cursor.callproc(name, parameters)
            self.__connector.commit()
            if self.__cursor.rowcount > 0:
                is_correct = True
            return (is_correct)
        except mysql.connector.Error as error:
            self.__connector.rollback()
            print(error)
            return (is_correct)
