import pandas as pd

df = pd.read_csv("./Data/pokemon_data.csv")
print(df.columns)

new = df[['Name','Speed']][0:4]
new2 = df.iloc[2:4]
print (new)
print ("Printing second table below")
print(new2)
print ("Done printing second table")

# Printing by row in for loop:
#for index, row in df.iterrows():
 #   print(index,row['Name'])

# Sorting columns by HP: 
sortd = df.sort_values('HP',ascending=False)
# Computing average using stats table in describe()
stats = sortd.describe()
avgattack = stats['Attack'][1]
print("Average attack = ",end='')
print(avgattack)

# Making changes to the table - adding and removing total columns
df['Total']= df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
print("Adding new column")
print(df.head(5))
df = df.drop(columns=['Total'])
print(df.head(5))

# Adding Total using different way, and then re-arranging columns
df['Total2'] = df.iloc[:,4:10].sum(axis=1)
print(df)
cols=list(df.columns.values)
df = df[cols[0:4]+[cols[12]]+cols[4:12]]
print(df.head(5))

df.to_csv('./Data/Modified.csv',index=False)
df.to_excel('./Data/modifiedxls.xlsx',index=False)

print ("Above 300 Total, and Grass and Poison:")
above300=df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['Total2']>300)]
print(above300)

print ("Below 300 Total:")
below300=df.loc[df['Total2']<300]
print(below300)

#To reset index:
above300 = above300.reset_index(drop=True)
#print(above300)

#Subjective changes (Multiple)
df.loc[df['Type 1'] == 'Fire', ['Legendary', 'Generation']] = [True, '0']
#print(df)

#Groupby (aggregate statistics)
group=df.groupby(['Type 1']).mean().sort_values('Defense',ascending=False)
print(group)
group=df.groupby(['Type 1']).sum()
print(group)
group=df.groupby('Type 1').count()
print(group)

#Create new empty dataframe with same columns
new_df = pd.DataFrame(columns=df.columns)

#Working with large amounts of data
new_df=new_df
for df in pd.read_csv('./Data/pokemon_data.csv', chunksize=5):
   print("Chunk dataframe:")
   print(df)
   new_df = pd.concat([new_df,df])
print(df)
print(new_df.head(50))