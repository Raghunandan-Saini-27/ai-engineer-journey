import pandas as pd

df=pd.read_csv("data/raw_data.csv")

new_row=df['salary_in_lakhs'] = df['salary'] / 100000

print(df.query("age>30"))

df.to_csv("data/raw_data.csv",index=False)