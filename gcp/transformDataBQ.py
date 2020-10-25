from google.cloud import storage,bigquery
from utils.getClient import getStorageClient,getBQClient
from utils.transformData import transformMeasures
import pandas as pd

bq_client = getBQClient()

def getDataset(dataset_name):
    """
        Get the bigquery dataset
    """
    # Create if not exists
    if dataset_name not in [x.dataset_id for x in bq_client.list_datasets()]:
        bq_client.create_dataset(dataset_name,timeout=30)
        print('Dataset {} created.'.format(dataset_name))

    return bq_client.dataset(dataset_name)


def loadTransformData(date):
    """
        Load csv from environment agency api transform and write to bigquery table
    """
    url = 'https://environment.data.gov.uk/flood-monitoring/archive/readings-full-{}.csv'.format(date)
    df = pd.read_csv(url)
    df = transformMeasures(df)
    # Get bigquery dataset
    dataset = getDataset('riverlevels')
    # Create bigquery from dataframe
    tablename = '{}.measurements'.format(dataset.dataset_id)
    df.to_gbq(tablename,if_exists='append')


loadTransformData('2020-10-23')