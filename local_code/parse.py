import os
import time
from urllib.parse import urlencode

import requests
import pandas as pd
from datetime import datetime

from constants import (
    FORMED_API_URL,
    LICENCES_TO_USE,
    BATCH_SIZE
)
from local_code.config import (
    UPPER_BOUND,
    LOWER_BOUND, CURRENT_TAXON_ID,
    USE_QUERY_PARAM, CURRENT_QUERY_PARAM, BASE_PREFIX_DIR, FAILED_RESOURCE_TIME_SLEEP, FAILED_LICENCE_TIME_SLEEP
)
from local_code.utils.data_formaters import single_table_format_inaturalist_data

# Function to ensure directories exist
def ensure_directory_exists(directory_path):
    os.makedirs(directory_path, exist_ok=True)

def form_params():
    params_dict = {
        "verifiable": "true",
        "order_by": "id",
        "order": "desc",
        "page": "1",
        "spam": "false",
        "photo_license": "cc-by",
        "photos": "true",
        "taxon_id": str(CURRENT_TAXON_ID),
        "locale": "en-US",
        "per_page": str(BATCH_SIZE),
        "return_bounds": "true",
    }

    if USE_QUERY_PARAM:
        params_dict["q"] = CURRENT_QUERY_PARAM
    return params_dict

def check_write_directories():
    directories_to_create_if_not_exist = [
        BASE_PREFIX_DIR,
        f"{BASE_PREFIX_DIR}/failed_licence",
        f"{BASE_PREFIX_DIR}/observations",
        f"{BASE_PREFIX_DIR}/failed_resource",
    ]
    [ensure_directory_exists(dir_to_check) for dir_to_check in directories_to_create_if_not_exist]

check_write_directories()
params = form_params()

for page_number in range(LOWER_BOUND, UPPER_BOUND):
    current_params = params.copy()
    current_params["page"] = str(page_number)
    for licence_to_use in LICENCES_TO_USE:

        current_params["photo_license"] = licence_to_use

        response = requests.get(FORMED_API_URL, params=current_params)
        failed_licence_urls = list()
        licence_observations = list()
        failed_resource_urls = list()
        i = 0  # In cases when specific license does not have observations
        if response.status_code == 200:
            for i, curr_res in enumerate(response.json()['results']):
                curr_start_time = datetime.now()
                curr_id = curr_res['id']

                curr_url = f"{FORMED_API_URL}/{curr_id}?include_new_projects=true&preferred_place_id=&locale=en-US&ttl=-1"
                curr_response = requests.get(curr_url)

                if curr_response.status_code == 200:
                    result_data = curr_response.json()['results']
                    formated_data = single_table_format_inaturalist_data(result_data, curr_id)
                    licence_observations.extend(formated_data)
                else:
                    print(
                        f"Server returned status code: {curr_response.status_code} for observation {curr_id}. Setting sleep for 60 seconds...")
                    failed_resource_urls.append({"url": curr_url, "status_code": curr_response.status_code})
                    time.sleep(FAILED_RESOURCE_TIME_SLEEP)

                if i != 0 and i % BATCH_SIZE == 0:
                    # print(licence_observations) # has been uncommented
                    df_licence_observations = pd.DataFrame(licence_observations)
                    df_licence_observations.to_parquet(
                        f'{BASE_PREFIX_DIR}/observations/observations_photo_batch_{page_number}_{licence_to_use}_{i}_{BATCH_SIZE}.parquet',
                        index=False)
                    licence_observations = list()

                end_time = datetime.now()
                print(f"Step {i} execution time:", end_time - curr_start_time)

        else:
            print(f"Server returned status code: {response.status_code}! In main for loop. Sleeping for 120 seconds")
            failed_licence_urls.append({"url": f"{FORMED_API_URL}?{urlencode(current_params)}",
                                        "status_code": response.status_code})
            # TODO: check this part with add parameters and write restoring script on file from duckdb and dbeaver
            time.sleep(FAILED_LICENCE_TIME_SLEEP)

        df_failed_licence = pd.DataFrame(failed_licence_urls)
        df_failed_licence.to_parquet(
            f'{BASE_PREFIX_DIR}/failed_licence/failed_licence_urls_{page_number}_{licence_to_use}.parquet',
            index=False)

        df_licence_observations = pd.DataFrame(licence_observations)
        df_licence_observations.to_parquet(
            f'{BASE_PREFIX_DIR}/observations/observations_photo_batch_{page_number}_{licence_to_use}_{i + 1}_{BATCH_SIZE}.parquet',
            index=False)

        df_failed_resource_urls = pd.DataFrame(failed_resource_urls)
        df_failed_resource_urls.to_parquet(
            f'{BASE_PREFIX_DIR}/failed_resource/failed_resource_urls_{page_number}_{licence_to_use}.parquet',
            index=False)
