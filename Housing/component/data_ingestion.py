from Housing.entity.config_entity import DataIngestionConfig
from Housing.exception import HousingException
import sys,os
from Housing.logger import logging

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data Ingestion Log Started.{'='*20}")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise
    