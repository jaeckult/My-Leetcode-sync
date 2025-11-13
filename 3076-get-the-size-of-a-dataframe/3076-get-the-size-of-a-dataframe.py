import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    #the question asks for a calculation and displaying of the number of rows and columns of players
    rows, columns = players.shape
    shape_list = [rows, columns]
    return shape_list
