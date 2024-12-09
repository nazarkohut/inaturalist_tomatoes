import pandas as pd
import requests
import os

# Load the CSV file into a DataFrame
file_path = '../raw_data/new_columns_general_and_7_diseases_202412011734.csv'
parsed_data = pd.read_csv(file_path)

# Extract the relevant columns (you can adjust these column names based on your CSV structure)
image_urls = parsed_data['original_image_url'].tolist()  # The column containing the S3 image URLs
roboflow_names = parsed_data['roboflow_file_name'].tolist()  # The column with the desired Roboflow names

# Folder to save images
output_folder = "downloaded_images"
os.makedirs(output_folder, exist_ok=True)

# List to store failed downloads
failed_downloads = []

# Function to download a file
def download_file(url, output_folder, filename=None):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for HTTP errors
        # Use the filename if provided, otherwise use URL's basename
        filename = filename or os.path.basename(url)
        file_path = os.path.join(output_folder, filename)
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        failed_downloads.append({"url": url, "filename": filename, "error": str(e)})

# Loop over each URL and corresponding file name to download the images
for i, (url, roboflow_name) in enumerate(zip(image_urls, roboflow_names)):
    # Download the image
    download_file(url, output_folder, filename=roboflow_name + ".jpg")  # You can change the file extension if needed
    print(f"Iteration number: {i}")

# If there are failed downloads, save them to CSV or Parquet
if failed_downloads:
    failed_df = pd.DataFrame(failed_downloads)
    # Save to CSV
    failed_df.to_csv("failed_downloads/failed_downloads.csv", index=False) # TODO: put some unique identifier in case of redownload

print("All images downloaded successfully!")

# Inform about failed downloads
if failed_downloads:
    print(f"Some downloads failed. Check 'failed_downloads.csv' for details.")
else:
    print("All downloads were successful.")
