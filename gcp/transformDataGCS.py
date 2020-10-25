from google.cloud import storage
from utils.getClient import getStorageClient
from utils.transformData import transformMeasures
import pandas as pd

storage_client = getStorageClient()

def getBucket():
    """
        Get the temporary storage bucket
    """
    bucket_name = 'tempdata_riverlevels'
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = 'STANDARD'

    # Check bucket doesnt exist and create 
    if not bucket.exists():
        bucket.create()
        print("Bucket {} created".format(bucket_name))

    return bucket


def loadTransformData(date):
    """
    Load csv from environment agency api transform and write to gcp bucket
    """
    url = 'https://environment.data.gov.uk/flood-monitoring/archive/readings-full-{}.csv'.format(date)
    df = pd.read_csv(url)
    df = transformMeasures(df)
    # Get temp bucket and upload cleaned csv
    bucket = getBucket()
    bucket.blob('tmpdata-{}.csv'.format(date)).upload_from_string(df.to_csv(),'text/csv')


loadTransformData('2020-10-23')