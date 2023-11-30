# To use Numpy and pandas to generate a list.
import pandas as pd
import numpy as np 

ser=pd.Series()
print("Pandas Series: ",ser)

data=np.array(['g','e','e','k','s'])

ser=pd.Series(data)
print("pandas series :\n",ser) 
