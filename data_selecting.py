Q1----2880 

Here we have been given a table in which we have 3 columns called student_id, name, and age
-- The question is we have to find the solution for selecting the columns with student name = 101 and the respective name and age column.
So here we will use the return statement so that we can get the exact column which we need.
So the solution code will be

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101 , ["name" , "age"]]


Q2----2881

In This question, we have to create a new column that has twice the values of the salary columns.
Here we have the name and salary
    
