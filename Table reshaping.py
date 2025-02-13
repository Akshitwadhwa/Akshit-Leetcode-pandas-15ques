Q1)
2888 -- Reshape Data , concaenate

import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    # here we just need to perform a simple concatitate 
     return pd.concat([df1,df2],axis=0)


here we had been given two dataframe tables known as df1 and df2.It has similiar columns to each other but there were no repeated values
We have to simply concatinate the two dataframes and make it as new single one.
So we use the pd.conat command

----------


Q2)
2889 --- Reshape.Pivot

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    newtabele = weather.pivot(index = 'month', columns = 'city',values='temperature')
    return newtabele
    # we have to join the table such that there are cities given in the input are there in the different city

Imp


