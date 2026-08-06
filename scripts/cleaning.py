import pandas as pd

def clean_column_names(df):
    df.columns = (df.columns
                  .str.lower()
                  .str.strip()
                  .str.replace(' ', '_')
                  .str.replace(r'[^a-z0-9_]', '', regex=True))
    return df