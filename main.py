import pandas as pd



df =  pd.read_csv('survey-lung-cancer.csv')
df.columns

[column + "_FLAG" if df[column].dtypes != "O" else column for column in df.columns]

[column + "_FLAG" if df[column].dtypes == "O" else 'NO_' + column if df[column].dtype == 'int64' else column for column in df.columns]



df.columns = [column.replace(" ","_") for column in df.columns]

new_cols = [column for column in df.columns if 'GENDER' in column or 'AGE' in column or 'LUNG_CANCER' in column]
new_df = df[new_cols]