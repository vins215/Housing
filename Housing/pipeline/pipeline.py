import os,sys
from Housing.config.configuration import Configuartion
from Housing.logger import logging
from Housing.exception import HousingException
from Housing.entity.aftifact_entity import DataIngestionArtifact
from Housing.entity.config_entity import DataIngestionConfig
from Housing.component.data_ingestion import DataIngestion


class Pipeliine:
    def __init__(self,config:Configuartion = Configuartion()) -> None:
        try:
            self.config = config

        except Exception as e :
            raise HousingException (e,sys) from e 
        
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion  =  DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())

            return data_ingestion.initiate_data_ingestiion()

        except Exception as e:
            raise HousingException(e,sys) from e
        
    def start_data_validation(self):
        pass

    def start_data_transformation(self):
        pass

    def start_model_trainer(self):
        pass

    def start_model_evaluation(self):
        pass

    def start_model_pusher(self):
        pass
    
    
    
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise HousingException(e,sys) from e

        