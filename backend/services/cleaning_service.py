from datetime import datetime
from backend.services.dataset_service import get_dataset, set_dataset

def remove_duplicates():

    df = get_dataset()

    if df is None:
        return "No dataset uploaded."

    before = len(df)

    df.drop_duplicates(inplace=True)

    after = len(df)

    removed = before - after

    return f"Removed {removed} duplicate rows."

def clean_dataset():

    df = get_dataset()

    if df is None:
        return "No dataset uploaded."

    before_rows = len(df)
    before_duplicates = df.duplicated().sum()

    cleaned_df = df.drop_duplicates()

    set_dataset(cleaned_df)

    after_rows = len(cleaned_df)
    after_duplicates = cleaned_df.duplicated().sum()

    return (
        f"Rows Before: {before_rows}, "
        f"Rows After: {after_rows}, "
        f"Duplicates Before: {before_duplicates}, "
        f"Duplicates After: {after_duplicates}"
    )

def export_cleaned_dataset():

    df = get_dataset()

    if df is None:
        return None

    file_path = f"uploads/cleaned_dataset_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

    df.to_excel(file_path, index=False)

    return file_path