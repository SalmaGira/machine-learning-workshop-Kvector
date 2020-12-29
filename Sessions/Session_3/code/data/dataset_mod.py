import pandas as pd


df = pd.read_csv('500_Person_Gender_Height_Weight_Index.csv')
df['Gender'] = df['Gender'].map({'Male':1,'Female':0})
df = df[['Height','Weight','Gender']]

print(df)

df.to_csv('genderclass.csv', index=False)# as csv

#df.to_csv('modified.txt', index=False, sep='\t')# other formats
#df.to_excel('modified.xlsx', index=False)

#df.to_csv('modified_ind.csv')