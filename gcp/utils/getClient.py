"""
Get client for project/credentials config files
"""
from google.cloud import bigquery, storage
from google.oauth2 import service_account
import configparser
import os

config = configparser.ConfigParser()
config.read('gcp/config/gcp.conf')

projectname = config['GCP']['projectname']
credPath = config['GCP']['credentials']
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credPath

def getBQClient():
    return bigquery.Client(project=projectname)

def getStorageClient():
    return storage.Client(project=projectname)