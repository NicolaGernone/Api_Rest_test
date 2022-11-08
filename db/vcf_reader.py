from typing import List
import pandas as pd
import gzip

def readcsv(args):
    return pd.read_csv(args, header=None)


    

