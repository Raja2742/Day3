import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load dataset
df=pd.read_csv("iris.csv")
print("dataset is reed succesfully")

#read first 5 rows
print(df.head())

#read basicinfo
print("\n----Basic info----")
print(df.info())

#get summary statastics
print("\n---summary statistics---")
print(df.describe)

# #handel missing values
# df=df.dropna()#remove rows with missing value
# df=df.fillna(0,inplace=True)#fill with zero in missing values


# # #remove duplicates
# # df.drop_duplicates()

# #save clean datasets
# df.to_csv("cleaned_dataset.csv",index=False)
# print("cleaned data is saved")

#rename coloum for clarity
df.rename(columns={"sepal_length":"Sepal Length","sepal_weidth":"SEpal Weidth"},inplace=True)

# Filter example: Only rows where petal length > 1.5
filtered_df = df[df['petal_length'] > 1.5]
print(filtered_df.head())


# Scatter plot
sns.scatterplot(x='Sepal Length', y='sepal_width', hue='species', data=df)
plt.title('Sepal Size by Species')
plt.show()

# Histogram
sns.histplot(df['petal_length'], bins=20, kde=True)
plt.title('Petal Length Distribution')
plt.show()

# Boxplot
sns.boxplot(x='species', y='petal_length', data=df)
plt.title('Petal Length by Species')
plt.show()