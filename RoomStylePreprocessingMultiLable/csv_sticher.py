import os
import pandas as pd


def create_summary_csv(root_dir: str) -> None:
    """
    Create a summary CSV file that consolidates information from multiple CSV files located in subdirectories of the root directory.

    Parameters:
    root_dir (str): The root directory path containing subdirectories with CSV files to consolidate.

    Returns:
    None: The function writes a new CSV file to the root directory that summarizes the information from all subdirectories.
    """

    # Get a list of all subdirectories in the root directory
    dirs = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]

    dfs = []
    for d in dirs:
        csv_path = os.path.join(root_dir, d, 'output.csv')
        if os.path.exists(csv_path):
            # Read the CSV file into a pandas dataframe and select the 'Name' and 'Status' columns
            df = pd.read_csv(csv_path)
            df = df[['Name', 'Status']]

            # Convert the 'Status' column to lowercase and map 'positive' to 1 and 'negative' to 0
            df['Status'] = df['Status'].str.lower()
            df['Status'] = df['Status'].map({'positive': 1, 'negative': 0})

            # Rename the 'Status' column to the subdirectory name and append the dataframe to the list
            df.rename(columns={'Status': d}, inplace=True)
            dfs.append(df.set_index('Name'))

    # Concatenate the dataframes horizontally and write the resulting merged dataframe to a new CSV file
    merged = pd.concat(dfs, axis=1)
    merged.reset_index(inplace=True)
    merged.to_csv(os.path.join(root_dir, 'summary.csv'), index=False)


if __name__ == '__main__':
    # Sample usage
    root_dir = '/media/mmohseni/ubuntu/storage/RoomStyles_labels_Operations/141020311 -Output- bucket_1'
    create_summary_csv(root_dir)
