import logging
import os
from datetime import datetime

# custom logging code (so that i can capture all the things that are executed )


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"   # setting logs file name
log_path = os.path.join(os.getcwd(),"logs",LOG_FILE)  # from where the file is executed it takes that path and create a logs folder there, and on their logs files will be builds 
# to make the folder
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)   # it is the complete "log file" path


#   >--- How the Log MESSAGE look like---<
# it has path of log file , what will be the format of the log file all these things should be defined in basicConfigs folders

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)