import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # students['name'] = students['name'].replace('null', pd.NA)  # convert string 'null' to actual NaN
    # students = students.dropna(subset['name'])                 # drop all rows with any NaN values
    
    students = students.dropna(subset=['name'])
    return students
