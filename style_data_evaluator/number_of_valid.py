import pandas as pd
import os

root_path = 'second_bucket'
list_ = os.listdir(root_path)

val = 0
non_val = 0
for i in list_:
    path = os.path.join(root_path,i)

    # Read the CSV file into a DataFrame
    df = pd.read_csv(os.path.join(path,'results.csv'))

    # Count the occurrences of 'not-valid' and 'valid' in the 'Validity' column
    validity_counts = df['Validity'].value_counts()

    # Retrieve the counts for 'not-valid' and 'valid'
    not_valid_count = validity_counts.get('not-valid', 0)
    valid_count = validity_counts.get('valid', 0)

    val = val + valid_count
    non_val = non_val + not_valid_count
    print(100 *'*')
    print(f'for class {i}')
    # Print the results
    print("Number of 'not-valid':", not_valid_count)
    print("Number of 'valid':", valid_count)
    print(f'Error Percentage : {not_valid_count/(not_valid_count+valid_count)*100}')

print(100*'==')
print(100*'==')
print(f' val = {val}')
print(f' non val = {non_val}')
print(f'FinallError Percentage : {non_val/(val+non_val)*100}')
