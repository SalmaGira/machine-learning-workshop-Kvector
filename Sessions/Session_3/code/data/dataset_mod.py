import pandas as pd


df = pd.read_csv('data/class.csv')


df['test1^2'] = df['test1']**2
df['test2^2'] = df['test2']**2
df['test1xtest2'] = df['test1']*df['test2']

df = df[['test1','test2','test1^2','test2^2','test1xtest2','admission']]
print(df)
df.to_csv('modified.csv', index=False)# as csv

#df.to_csv('modified.txt', index=False, sep='\t')# other formats
#df.to_excel('modified.xlsx', index=False)

#df.to_csv('modified_ind.csv')