#logger is for purpose thst any execution that happens we should be able to log all the execution, 
# including execution, error details, and everything into a text file
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format= "[%(asctime)s]%(lineno)d %(name)s - %(levelname)s - %(mesage)s",
    level = logging.INFO,
)
