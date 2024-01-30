import pandas as pd

excel_file_path = 'MIC_STUDY_DATA.xlsx'

df = pd.read_excel(excel_file_path)

# Read headers
# print (df.columns)*

# Read specific column
# Print (df[Column name(s)] [range of columns])*

# Read each row
# print(df.head(4))
# print (df.iloc[row number(s)])

# iterate through rows
# for index, row in df.iterrows():
    #print (index, row)

# Read specific location
# print (df.iloc[row number, column number])

#df.loc[df["column name"] == "something"]

#Adding column
#df[''] = df['']+df['']...
# df = df.drop(columns = [''])

# Summing multiple columns
# df [''] = df.iloc[:, 4:9].sum(axis=1)

#Rearrange column
# cols = list (df.columns.values)
#df = [cols[0:4] + [cols[-1]] + cols [4:12]


# Saving data
#df.to_excel('name.xlsx')



#Filtering data
# df.loc[df['Name of a column'] == 'Something']]
#multiple 
# df.loc[(df['Name of a column'] == 'Something') & (df['Name of a column] == 'Something else')]
#To just separate it
#new_df = df.loc[(df['Name of a column'] == 'Something') & (df['Name of a column] == 'Something else')]
# And to save this filtered data
# new_df.to-excel('name for it')


# Regex filtering
# df.loc[df['Name'].str.contains('String')]
# To get the reverse of the above
# df.loc[~df['Name'].str.contains('String')]

# More Regex filtering
# import re 
# df.loc[df['Column'].str.contains('thing'|'other thing'), regex=True]

# Conditional changes
# df.loc[df['Column'] == 'A string', 'The column (parameter)'] = 'New name'

#Multiple parameters change
# df.loc[df['column'] > 500, ['column', 'other column'] = 'Test value'

# Aggregate statistics with groupby
# df.groupby(['Column]).mean().sort_values('Parameter', ascending)
