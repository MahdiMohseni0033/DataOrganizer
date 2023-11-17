import pandas as pd

# Read the CSV files
df1 = pd.read_csv('/media/mmohseni/ubuntu/storage/RoomStyles_labels_Operations/141020311 -Output- bucket_1/bucket_1.csv')
df2 = pd.read_csv('/media/mmohseni/ubuntu/storage/RoomStyles_labels_Operations/14020424_Output_bucket_2/bucket_2.csv')

# Merge the dataframes using the 'concat' function
merged_df = pd.concat([df1, df2])

# Write the merged dataframe to a new CSV file
merged_df.to_csv('merged_file.csv', index=False)