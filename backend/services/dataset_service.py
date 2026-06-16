import pandas as pd

current_df = None

def load_dataset(file_path):
    global current_df

    if file_path.endswith(".csv"):
        current_df = pd.read_csv(file_path)

    elif file_path.endswith(".xlsx"):
        current_df = pd.read_excel(file_path)

    return current_df

def get_dataset():
    return current_df

def set_dataset(df):
    global current_df
    current_df = df