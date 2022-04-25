import pandas as pd
import numpy as ny
squad = {'Batsmen': {'Rohit Sharma': {'Matches': 206,
                                      'Runs': 8010,
                                      'Average':47.4,
                                      'Highest Score': 264 },
                     'Shikhar Dhawan': {'Matches':128,
                                        'Runs': 5355,
                                        'Average': 44.62,
                                        'Highest Score': 143},
                     'Virat Kohli': {'Matches': 227,
                                     'Runs': 10843,
                                     'Average': 59.58,
                                     'Highest Score': 183}}}
df = pd.DataFrame(squad['Batsmen'])
print(df)
