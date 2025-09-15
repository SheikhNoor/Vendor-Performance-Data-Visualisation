import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time
logging.basicConfig(
    filename="E:/Vendor Project/log/ingestion_db.log",
    level = logging.DEBUG,
    format= "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filemode="a"
)
engine = create_engine('sqlite:///inventory.db')

def ingest_db(chunk, table_name, engine):
    chunk.to_sql(table_name, con=engine, if_exists='append', index=False)
def load_raw_data():
    start = time.time()
    for file in os.listdir('E:/Vendor Project/data'):
        if '.csv' in file:
            table_name = file[:-4]
            logging.info(f"Ingesting {table_name} in database")
            for chunk in pd.read_csv('E:/Vendor Project/data/'+file, chunksize=100000):  # adjust chunksize as needed
                ingest_db(chunk, table_name, engine)
    end = time.time()
    total_time = (end-start)/60
    logging.info("Finished ingesting data")
    logging.info(f"Total time: {total_time} minutes")

if __name__ == "__main__":
    load_raw_data()