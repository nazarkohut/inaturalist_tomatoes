import os
import pandas as pd
import pyarrow.parquet as pq

def process_parquet_files(directory, output_path, columns, filename_prefix="observations_photo_"):
    """
    Processes Parquet files in the specified directory:
    - Appends URLs of non-empty files to a list.
    - Writes headers to empty Parquet files.
    - Saves URLs of non-empty files to a specified output Parquet file.

    Parameters:
    directory (str): Directory path containing Parquet files.
    output_path (str): Path to save the output Parquet file with URLs.
    columns (list of str): List of column names for the DataFrame.
    filename_prefix (str): Optional prefix for filtering files (default is "observations_photo_").
    """
    # List to hold all file URLs
    file_urls = []

    # Loop through all files in the specified directory
    for filename in os.listdir(directory):
        # Check if the file name starts with the desired prefix and is a Parquet file
        if filename.startswith(filename_prefix) and filename.endswith(".parquet"):
            file_path = os.path.join(directory, filename)

            # Check if the file is non-empty (contains at least one row)
            try:
                parquet_file = pq.ParquetFile(file_path)
                row_count = parquet_file.metadata.num_rows
                if row_count > 0:
                    # Store the file URL (full path) in the list
                    file_urls.append([file_path])  # Append the file URL as a list (for DataFrame format)
                    print(f"Added file: {file_path}")  # Optionally print each added file URL
                else:
                    # If the file is empty, create an empty DataFrame with the column headers
                    empty_df = pd.DataFrame(columns=columns)
                    empty_df.to_parquet(file_path, engine='pyarrow')  # Write empty DataFrame with column headers
                    print(f"Created empty file with headers: {file_path}")
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

    # Create a DataFrame from the list of URLs
    df = pd.DataFrame(file_urls, columns=["file_url"])

    # Write the DataFrame to a Parquet file
    df.to_parquet(output_path, engine='pyarrow')

    print(f"All valid file URLs have been written to {output_path}")
