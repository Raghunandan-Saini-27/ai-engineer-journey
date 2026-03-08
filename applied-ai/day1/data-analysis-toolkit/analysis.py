import pandas as pd
df=pd.read_csv("data/sales_data.csv")				#Load dataset 

print(df.head())									#First Rows

df["revenue"]=df["price"]*df["quantity"]			#New Revenue column added
print("Revenue :\n",df["revenue"])

print("Total Revenue : ",df["revenue"].sum())		#Total Revenue

print("Most Sold Product : ",df.loc[df["quantity"].idxmax()]["product"])	#Most sold product

print("Avg. Product Price : ",round(df["price"].mean(),2))	#Avg Price

print("Grouped by ",df.groupby("category")["revenue"].sum())	#Group by category