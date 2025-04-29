import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    new_students = students.dropna()
    return students.dropna(subset=['name'])
