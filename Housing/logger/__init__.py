import logging
from datetime import datetime
import os

Log_Dir = "Housing_Logs"
Current_time_stamp = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
Log_file_name = f"log_{Current_time_stamp}.log"
os.makedirs(Log_Dir , exist_ok=True)
Log_file_path = os.path.join(Log_Dir,Log_file_name)
logging.basicConfig(filename=Log_file_path ,filemode="w",
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)