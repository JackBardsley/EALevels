import pandas as pd

def transformMeasures(df):
    # Select cols
    df = df[['dateTime','date','label','stationReference','parameter','qualifier','period','unitName','valueType','value']]
    # Drop rows without measures/dates/stations
    df.dropna(subset=['dateTime','value','stationReference'],inplace=True)
    # Clean values containing pipe symbol
    df['value'] = df['value'].apply(lambda x: str(x).split('|')[-1])
    # Convert column types
    df['value'] = df['value'].astype('float')
    df['dateTime'] = df['dateTime'].astype('datetime64')
    return df