from mushroom.entity.config_entity import DataIngestionConfig
from mushroom.exception import MushroomException
from mushroom.logger import logging
#from mushroom.utils.main_utils import read_yaml_file
import sys,os
import pandas as pd
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise MushroomException(e,sys) from e

    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            pass
            # df = pd.read_csv(self.data_ingestion_config.dataset_download_url)
            # logging.info("Read the dataset as dataframe")

            # os.makedirs(os.path.dirname(self.data_ingestion_config.ingested_train_dir),exist_ok=True)
            # df.to_csv(self.data_ingestion_config.ingested_train_dir,index=False,header=True)

            # logging.info("Ingestion of the data is completed")

            # return self.data_ingestion_config

        except Exception as e:
            raise MushroomException(e,sys) from e