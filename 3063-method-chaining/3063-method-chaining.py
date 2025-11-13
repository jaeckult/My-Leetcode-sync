import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where weight > 100
    heavy_animals = animals[animals['weight'] > 100]
    
    # Sort by weight descending
    heavy_animals_sorted = heavy_animals.sort_values(by='weight', ascending=False)
    
    # Return only the 'name' column
    return heavy_animals_sorted[['name']]
