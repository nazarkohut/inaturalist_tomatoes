import numpy as np
import pandas as pd
from roboflow import Roboflow

from local_code.roboflow.upload_config import METADATA_FILE, \
    IMAGE_DIR_PATH, IS_POSSIBLY_LABELED_SUBSET, INATURALIST_TO_OWN_ANNOTATIONS, \
    ALL_ANNOTATIONS_MAPPING, BATCH_SIZE_OF_SLICE, BATCH_PART
from local_code.roboflow.utils.upload_config_constants import API_KEY, WORKSPACE_ID, PROJECT_ID

# Load the metadata
metadata_df = pd.read_csv(METADATA_FILE)
if not IS_POSSIBLY_LABELED_SUBSET:
    metadata_df = metadata_df.iloc[(BATCH_SIZE_OF_SLICE * BATCH_PART) : (BATCH_SIZE_OF_SLICE * (BATCH_PART + 1))]

# Initialize Roboflow API
rf = Roboflow(api_key=API_KEY)

project = rf.workspace(WORKSPACE_ID).project(PROJECT_ID)

failed_upload_results = []

# Upload images with tags
for index, row in metadata_df.iterrows():

    image_path = f"{IMAGE_DIR_PATH}{row['roboflow_file_name']}.jpg"  # Path to the image
    license_code = row['license_code']
    attribution = row['attribution']
    place_guess = row['place_guess']
    observed_on_date = row['observed_on_date']
    quality_grade = row['quality_grade']

    annotation = row['english_common_name']
    alternative_annotation = row['preferred_common_name']

    actual_annotation = annotation if annotation and annotation != "unidentified" \
        else alternative_annotation if alternative_annotation and alternative_annotation != "unidentified" else "other"

    actual_annotation = actual_annotation if actual_annotation is not np.nan else "other"

    if (
            (actual_annotation in INATURALIST_TO_OWN_ANNOTATIONS and not IS_POSSIBLY_LABELED_SUBSET)
            or
            (actual_annotation not in INATURALIST_TO_OWN_ANNOTATIONS and IS_POSSIBLY_LABELED_SUBSET)
    ):
        print(f"Skipping image as annotation of {actual_annotation} is not in subset we are working with.")
        continue

    actual_annotation = ALL_ANNOTATIONS_MAPPING[actual_annotation]

    # Create a combined tag string or list
    tags = [license_code, attribution, place_guess, observed_on_date, quality_grade]

    try:
        # Upload the image with tags
        response = project.upload(
            image_path=image_path,
            annotation_path=actual_annotation,
            tag_names=tags
        )
        print(f"Uploaded: {image_path} with response: {response}")
    except Exception as e:
        # Only record failures
        failed_upload_results.append({
            'image_path': image_path,
            'status': 'Failure',
            'error_message': str(e)
        })

        print(f"Failed to upload {image_path}: {e}")


# Create a DataFrame from the failed results list
if failed_upload_results:
    failed_upload_results_df = pd.DataFrame(failed_upload_results)
    # Save the result to a CSV file
    output_csv_path = f"failed_uploads/upload_failures_{PROJECT_ID.replace('-', '_')}.csv"
    failed_upload_results_df.to_csv(output_csv_path, index=False)
    print(f"Upload failures saved to {output_csv_path}")
else:
    print("No upload failures.")

