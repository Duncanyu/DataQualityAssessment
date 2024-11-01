from pandas import *

#Data quality assessment

file_path = "sample_data/process.csv"
df = read_csv(file_path)

#print(df.head(4))

def count_empty(row):
    empty_columns = [col for col in df.columns if isna(row[col] or str(row[col]).strip == '')]
    return len(empty_columns), ', '.join(empty_columns)

df['No_of_EmptyCell'] = (df.apply(lambda row: count_empty(row)[0], axis = 1))
df['List_of_Empty_Col_Name'] = (df.apply(lambda row: count_empty(row)[1], axis = 1))

first_column = df.pop('No_of_EmptyCell')
second_column = df.pop('List_of_Empty_Col_Name')

df.insert(0, 'No_of_EmptyCell', first_column)
df.insert(1, 'List_of_Empty_Col_Name', second_column)

df.to_csv('processed.csv', index = False)
