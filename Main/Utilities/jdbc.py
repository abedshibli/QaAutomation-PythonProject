from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector


class JDBC:

    bank_details = []

    @staticmethod
    def connect_db():
        globals()["my_db"] = mysql.connector.connect(
            host="remotemysql.com",
            database='Y8Nkn2FnBq',
            user="Y8Nkn2FnBq",
            password="kLrc4xtpod"
        )
        return globals()["my_db"]

    @staticmethod
    def get_bank_list_details():
        query = "SELECT bank,account,routing FROM ness"
        my_cursor = globals()["my_db"].cursor()
        my_cursor.execute(query)
        JDBC.bank_details = my_cursor.fetchall()
        return JDBC.bank_details
