import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products = products.fillna({'quantity': 0})
    return products