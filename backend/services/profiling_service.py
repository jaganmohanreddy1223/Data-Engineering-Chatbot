from backend.services.dataset_service import get_dataset

def generate_summary():

    df = get_dataset()

    if df is None:
        return "No dataset uploaded."

    summary = f"""
Rows: {df.shape[0]}
Columns: {df.shape[1]}
Duplicate Rows: {df.duplicated().sum()}

Column Names:
{', '.join(df.columns)}
"""

    return summary