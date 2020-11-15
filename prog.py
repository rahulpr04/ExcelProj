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


