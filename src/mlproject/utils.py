# reading of the data can be done in this file

import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

# this will load the information from .env folder
load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


def read_sql_data():
    logging.info("Reading SQL database is started")
    
    try:
        mydb = pymysql.connect(
            host = host,
            user=user,
            password=password,
            db = db
        )
        logging.info("Connection Established",mydb)
        
        df = pd.read_sql_query('Select * from smartphones',mydb)
        print(df.head())
        
        return df 
    except Exception as ex:
        raise CustomException(ex)
    
