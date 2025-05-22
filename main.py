import pandas as pd
import seaborn as sns


df =  pd.read_csv('survey-lung-cancer.csv')
df.columns

[column + "_FLAG" if df[column].dtypes != "O" else column for column in df.columns]

[column + "_FLAG" if df[column].dtypes == "O" else 'NO_' + column if df[column].dtype == 'int64' else column for column in df.columns]

