import pandas as pd
import glob

def read_csv(path):
    csv_files = glob.glob(path + "/coin_*.csv")
    df_list = (pd.read_csv(file) for file in csv_files)
    df_values = pd.concat(df_list, ignore_index=True)
    return df_values.values


    

