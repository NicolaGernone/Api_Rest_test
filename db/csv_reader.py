import pandas as pd

def readcsv(path):
    csv_files = glob.glob(path + "/coin_*.csv")
    df_list = (pd.read_csv(file) for file in csv_files)
    return pd.concat(df_list, ignore_index=True)


    

