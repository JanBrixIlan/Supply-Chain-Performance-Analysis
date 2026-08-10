import pandas as pd

def clean_column_names(df):
    df.columns = (df.columns
                  .str.lower()
                  .str.strip()
                  .str.replace(' ', '_')
                  .str.replace(r'[^a-z0-9_]', '', regex=True))
    return df

def convert_dates(df):
    date_columns = [
        'order_date_dateorders',
        'shipping_date_dateorders',
    ]
    for col in date_columns:
        df[col] = pd.to_datetime(df[col],
                                   format='%m/%d/%Y %H:%M',
                                   errors='coerce')
    return df