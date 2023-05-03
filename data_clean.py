import pandas as pd

cols = ['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime',
        'passenger_count', 'trip_distance', 'RatecodeID',
        'store_and_fwd_flag', 'PULocationID', 'DOLocationID',
        'payment_type', 'fare_amount', 'extra',
        'mta_tax', 'tip_amount', 'tolls_amount', 'tripId']

dtypes = {
    'VendorID': 'float32',
    'tpep_pickup_datetime': 'str',
    'tpep_dropoff_datetime': 'str',
    'passenger_count': 'float32',
    'trip_distance': 'str',
    'RatecodeID': 'float32',
    'store_and_fwd_flag': 'str',
    'PULocationID': 'float32',
    'DOLocationID': 'float32',
    'payment_type': 'float32',
    'fare_amount': 'float32',
    'extra': 'float32',
    'mta_tax': 'float32',
    'tip_amount': 'float32',
    'tolls_amount': 'float32',
    'tripId': 'float32'
}


dframe = pd.read_csv('yellow_tripdata_2021-01_raw_updated.csv',
                     usecols = cols,
                     dtype=dtypes,
                     )

dframe['trip_distance'] = dframe['trip_distance'].str.replace('km', '')

dframe.to_csv('cleaned_df', index=False)


