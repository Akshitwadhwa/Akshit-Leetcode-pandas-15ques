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
( this is the modify columns question)
( In this we have to play with the data where we have to make a new salary columns with making it twice its orginal values
  
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary']  = employees['salary'] * 2
    return employees

--------


Q4--- 2885
(This is the rename columns question)
There is a table given with columns name such as id, first , last , age etc
-- We HAVE TO RENAME THE GIVEN columns so we use the .rename command along with the name of columns

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns = {'id':'student_id' , 'first': 'first_name' , 'last':'last_name' , 'age':'age_in_years'}, inplace=True)
    return students


-------

Q5-----2886
Change Data Type
Here we have to change the datatype of a column given to us 
The grade column is stored as float we have to convert it to int

So the code will be 

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(students)
    df['grade] = df[['grade']].astype(int)
    return df

--------


Q6----- 2887
(This is the fill missing data question)
We are going to use the fillna command in this question 
So We have to find the correct way to find to do that
The code will be 

import pandas as pd

def fillMissingValues(table: pd.DataFrame) -> pd.DataFrame:
    table['quantity'].fillna(0,inplace=True)
    return table


















