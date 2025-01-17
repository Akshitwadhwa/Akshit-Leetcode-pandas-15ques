we are going to first begin with the question 1 of the given leetcode question
This is 2878-
here we have to find the size of the dataset which is found by using the shape command

so the code will be 

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return[players.shape[0] , players.shape[1]]


(Q2)
Here we have to find the first 3 rows of the given table
it is a table so we will use a head command
for example if a dataset is ames
ames.head(3) is the way to find the first 3 rows

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

