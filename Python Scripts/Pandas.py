# All of these commands were used in Pandas module of Python within the Jupyter notebook. All inputs within '' are changed dependent of the user data.


import pandas as pd # Imports Pandas module of python



header_list = ['column_name_1', 'column_name_2'] # Creates headers names for each column circRNAs Tables


df = pd.read_csv('Example.txt', names = header_list, delimiter='\t') # Reads text file with columns separated by tabs, and creates a data frame with the chosen header_list names


df = df.drop(columns=['column_name_1']) # Drops a chosen column from a data frame


df = df.drop_duplicates(subset=['column_name_1'], keep=False) # Drops sequences with duplicates in a chosen column


df ['Sequence length'] = df ['Sequence'].str.len() # Adds a new column of sequence lengths for each circRNA sequence


df.sort_values('column_name_1', axis = 0, ascending = True) # Sorts a column by ascending values


Translatable_circRNA = df[df['Sequence length'] > 119] # Only keeps circRNA sequnces of lengths greater than 120 nts


dfs_merged = pd.merge(df_1, df_2, how='outer', on=['Column_1']) # Merges two dataframes on the chosen column


df.to_csv('Example.csv', index=False)  # creates an outfile in .csv format


df.to_csv('Example.txt', index=False, sep ='\t', header = None) # creates an outfile in .txt format with no headers and each column separated by a tab.
