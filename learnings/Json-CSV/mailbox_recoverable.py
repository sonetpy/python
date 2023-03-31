import pandas as pd
import csv
import re

# Load the first CSV file
df1 = pd.read_csv('MailboxSizeReports.csv')

# Load the second CSV file, excluding the first row
df2 = pd.read_csv('Recoverable_Items.csv', skiprows=[0])

# Select the specific columns from each file
cols_to_use1 = ['Name','PrimarySmtpAddress', 'TotalSizeInMB']
cols_to_use2 = ['DisplayName','UPN','Recoverable Size']
df1_subset = df1[cols_to_use1]
df2_subset = df2[cols_to_use2]

# merge the two dataframes on the matching columns
merged_df = pd.merge(df1_subset, df2_subset, left_on='Name', right_on='DisplayName')

# extract only bytes value from 6th row and skip any values with MB, KB, or GB
bytes_regex = r'(\d+(?:,\d+)*) bytes'
bytes_pattern = re.compile(bytes_regex)
byte_values = []

for row in merged_df['Recoverable Size']:
    byte_match = bytes_pattern.search(row)
    if byte_match:
        byte_values.append(int(byte_match.group(1).replace(',', '')))
    else:
        byte_values.append(None)

# add the byte values to a new column in the merged dataframe
merged_df['Recoverable Size in Bytes'] = byte_values

# Convert byte values to MB with two decimal points
merged_df['Recoverable Size in MB'] = merged_df['Recoverable Size in Bytes'] / (1024*1024)
merged_df['Recoverable Size in MB'] = merged_df['Recoverable Size in MB'].round(2)

# select only the columns we want to keep
merged_df_subset = merged_df[['Name', 'PrimarySmtpAddress', 'TotalSizeInMB', 'DisplayName', 'UPN', 'Recoverable Size in MB']]

# sort the merged dataframe based on the remaining columns
merged_df_sorted = merged_df_subset.sort_values(by=['TotalSizeInMB', 'Recoverable Size in MB'])

# calculate the sum of TotalSizeInMB and Recoverable Size in MB
merged_df_sorted['TotalSizeAndRecoverable'] = merged_df_sorted['TotalSizeInMB'] + merged_df_sorted['Recoverable Size in MB']

# check if the sum exceeds 150 GB and add a new column with the result
merged_df_sorted['Check If more than 150 GB'] = merged_df_sorted['TotalSizeAndRecoverable'].apply(lambda x: 'BAD' if x > 150100 else 'GOOD')

# write the merged and sorted dataframe to a new CSV file
merged_df_sorted.to_csv('merged_file.csv', index=False)

# print any rows with a total size exceeding 150 GB
bad_rows = merged_df_sorted[merged_df_sorted['Check If more than 150 GB'] == 'BAD']

if not bad_rows.empty:
    print('The following rows have a total size exceeding 150 GB:')
    print(bad_rows)
else:
    print('No rows have a total size exceeding 150 GB.')
