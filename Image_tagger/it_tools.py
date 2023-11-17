import os
import pandas as pd


def csv_merger(directory_path):
    """Merge multiple CSV files from a directory.

    Args:
        directory_path (str): The directory path where the CSV files are located.

    Returns:
        None

    Raises:
        FileNotFoundError: If the directory_path does not exist.

    Example:
        csv_merger('/path/to/csv/files/')

    """
    # Check if the directory path exists
    if not os.path.isdir(directory_path):
        raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

    # Initialize an empty DataFrame to store the merged data
    merged_data = pd.DataFrame(columns=['Name', 'Status'])

    # Loop through all CSV files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            # Read the CSV file into a DataFrame
            file_path = os.path.join(directory_path, filename)
            data = pd.read_csv(file_path)

            # Keep only the 'Name' and 'Status' columns
            data = data[['Name', 'Status']]

            # Append the data to the merged DataFrame
            merged_data = pd.concat([merged_data, data], ignore_index=True)

    # Write the merged data to a new CSV file
    merged_data.to_csv('merged_data.csv', index=False)


if __name__ == '__main__':
    pass
