from mushroom.pipeline.pipeline import Pipeline
from mushroom.exception import MushroomException
from mushroom.logger import logging
import sys,os

def main():
    # 1. Create an instance of the Pipeline class
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__ == '__main__':
    main()