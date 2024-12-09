import pandas as pd
import requests
import os

from local_code.roboflow.utils.upload_config_constants import WORKSPACE_ID, API_KEY, PROJECT_ID

# Load failure log
failure_log_path = "failed_uploads/upload_failures_inaturalist_tomatoes_part_1.csv"
failures = pd.read_csv(failure_log_path)

# Extract failed image paths
failed_images = failures['image_path']


UPLOAD_URL = f"https://api.roboflow.com/{WORKSPACE_ID}/{PROJECT_ID}/upload?api_key={API_KEY}"

# Attempt to re-upload images
for image_path in failed_images:
    try:
        # Check if the file exists
        if not os.path.exists(image_path):
            print(f"File not found: {image_path}")
            continue

        # Open the image file
        with open(image_path, 'rb') as image_file:
            # Make the upload request
            response = requests.post(
                UPLOAD_URL,
                files={"file": image_file},
                data={"name": os.path.basename(image_path)}
            )

        # Check response status
        if response.status_code == 200:
            print(f"Successfully re-uploaded: {image_path}")
        else:
            print(f"Failed to re-upload: {image_path}")
            print(f"Error: {response.json()}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

# TODO: check if it really does anything
