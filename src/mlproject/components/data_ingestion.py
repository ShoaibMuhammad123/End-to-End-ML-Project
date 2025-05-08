import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from src.mlproject.utils import read_sql_data

from sklearn.model_selection import train_test_split


from dataclasses import dataclass  # this is becoz all the input parameter we can initialze here (train_dataset_path,test_dataset_path)


# now i write my dataclass for this we use decorator of dataclass first
@dataclass
class DataIngestionConfig:
    # as we know that we need three data paths (train,test,raw data paths)
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','raw.csv')
    
    # the above information all will be stored in artifact folder

# now we define the class for DataIngestion

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        try:
            # Reading code  from mysql
            df = read_sql_data()  # raw data
            logging.info("Reading Complited from mysql database")
            
            # when data will be read then we have to store them on the files but before that we have to create the folder and files
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            # saving the data
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Data Ingestion is Completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
            
            
        except Exception as e:
            raise CustomException(e,sys)
        
