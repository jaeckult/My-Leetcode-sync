import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    weather_pivoted = weather.pivot(index='month', columns='city', values='temperature')
    return weather_pivoted