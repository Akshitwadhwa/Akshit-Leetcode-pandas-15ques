Q1--- 2882
Here we have a question where we have to delete a given column in a certain table so we will use the return command and drop command 
we have to remove the duplicate emails in the given data frame so the code will be

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates('email')
