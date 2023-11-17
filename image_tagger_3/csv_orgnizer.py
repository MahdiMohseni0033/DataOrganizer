import csv
import pandas as pd
from sklearn.model_selection import train_test_split


# Specify the input and output file names
def tag_reverser(desir_tag:str):
    input_file = 'valid.csv'
    output_file = 'valid_2.csv'

    # Open the input and output files
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        # Create a CSV reader and writer
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()

        # Loop through each row in the input file and swap the "carpet" values
        for row in reader:
            if row[desir_tag] == '0':
                row[desir_tag] = '1'
            elif row[desir_tag] == '1':
                row[desir_tag] = '0'
            writer.writerow(row)

    print(f"Successfully swapped values in the {desir_tag} column in {input_file} and saved the result in {output_file}.")


def tag_counter(csv_path):
    df = pd.read_csv(csv_path)

    # Select all columns except the first one (which contains the image names)
    tag_columns = df.columns[1:]

    # Use the sum() method to count the number of 1s in each tag column
    one_counts = df[tag_columns].sum()

    # Print the results
    print("Number of 1s in each tag column:")
    print(one_counts)


def split_csv_to_train_valid(csv_file_path, train_csv_file_path, valid_csv_file_path, test_size=0.2, random_state=42):
    """
    Read a CSV file containing labels for a multilabel classification task, and split the data randomly into a training set
    and a validation set using pandas.

    :param csv_file_path: The path to the input CSV file.
    :param train_csv_file_path: The path to the output training CSV file.
    :param valid_csv_file_path: The path to the output validation CSV file.
    :param test_size: The proportion of data to be included in the validation set (default is 0.2).
    :param random_state: The random seed to use for the train-test split (default is 42).
    """
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Split the data into training and validation sets
    train_df, valid_df = train_test_split(df, test_size=test_size, random_state=random_state)

    # Write the training and validation sets to CSV files
    train_df.to_csv(train_csv_file_path, index=False)
    valid_df.to_csv(valid_csv_file_path, index=False)

    print(
        f"Successfully split the CSV file '{csv_file_path}' into training and validation sets, and saved the result in "
        f"'{train_csv_file_path}' and '{valid_csv_file_path}'.")


if __name__ == '__main__':
    # split_csv_to_train_valid('merged_file.csv', 'train_.csv', 'valid_.csv')
    print('For train ')
    tag_counter('train_.csv')
    print('For valid')
    tag_counter('valid_.csv')
    # tag_reverser('parquet')