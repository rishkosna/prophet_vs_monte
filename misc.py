import json
import requests
import pandas
pandas.options.mode.chained_assignment = None  # default='warn'
import numpy
from datetime import *

def simple_df (df) :
    now = datetime.now()
    df.drop(df.index[df['close_date'] < date.today()], inplace=True)
    df.drop(df.index[df['close_date'] > date.today() + timedelta(2)], inplace=True)
    df.drop(df.index[df['yes_ask'] == 1], inplace=True)
    df.drop(df.index[df['yes_ask'] == 100], inplace=True)