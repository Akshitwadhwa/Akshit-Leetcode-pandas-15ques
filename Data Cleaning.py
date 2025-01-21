Q1--- 2882
Here we have a question where we have to delete a given column in a certain table so we will use the return command and drop command 
we have to remove the duplicate emails in the given data frame so the code will be

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates('email')

# Here we can see that the email has been dropped after this

Q2--- 2883
( This is a drop missing data question )
In the table there are 3 tables called student_id , name , age
We have to find the null value in the name column and remove that value.
So we will use the dropna command.

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
   return students.dropna(subset="name")

---------
Q3--- 2884
( In this we have to play with the data where we have to make a new salary columns with making 
