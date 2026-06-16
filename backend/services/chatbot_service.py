from backend.services.dataset_service import get_dataset
from backend.services.profiling_service import generate_summary
from backend.services.cleaning_service import remove_duplicates
from backend.services.cleaning_service import clean_dataset


def process_question(question):

    df = get_dataset()

    if df is None:
        return "Please upload a dataset first."

    question = question.lower()

    if "rows" in question:
        return f"The dataset contains {df.shape[0]} rows."

    elif "columns" in question:
        return f"The dataset contains {df.shape[1]} columns."

    elif "column names" in question:
        return ", ".join(df.columns)

    elif "missing" in question:
        missing = df.isnull().sum()
        missing = missing[missing > 0]
        return str(missing)

    elif "remove duplicates" in question:
        return remove_duplicates()

    elif "duplicate" in question:
        return f"Duplicate rows: {df.duplicated().sum()}"

    elif "summary" in question:
        return generate_summary()

    elif (
        "first 5 rows" in question
        or "head" in question
        or "top rows" in question
    ):
        return str(df.head())

    elif (
        "last 5 rows" in question
        or "tail" in question
        or "bottom rows" in question
    ):
        return str(df.tail())
    
    elif "clean dataset" in question:
    	return clean_dataset()

    elif "current rows" in question:
    	return f"Current rows: {len(df)}"

    else:
        return "Sorry, I don't understand that question yet."