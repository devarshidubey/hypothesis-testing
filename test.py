import pandas as pd
import numpy as np

np_arr = np.array([
    [1, 11, 3.5, '2022-01-01'],
    [2, 12, 4.2, '2022-01-02'],
    [3, 13, 4.1, '2022-01-03'],
    [4, 14, 3.8, '2022-01-04'],
    [5, 15, 2.9, '2022-01-05'],
    [10, 16, 4.5, '2023-11-27']
])

df = pd.DataFrame(np_arr, columns=['movieid', 'userid', 'rating', 'date'])
newdf = df[df['movieid'] == 10]
print(newdf)
