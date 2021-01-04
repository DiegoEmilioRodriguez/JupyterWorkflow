import os
from urllib.request import urlretrieve

import pandas as pd

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD&api_foundry=true'

def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL, force_download=False):
    """Download and cache the fremont data

    Parameter
    ---------
    filename : string(optional)
        location to save the data
    url : string(optional)
        web location of the data
    force_download : bool (optional)
        if True, force download of data
    
    Returns
    ----
    data : pandas.DataFrame
    the Fremont bridge data
    """
    

    if force_download or not os.path.exists(filename):
        urlretrieve(URL, 'Fremont.csv')
    data = pd.read_csv('Fremont.csv', index_col='Date', parse_dates=True)
    return data
