import time

import requests
import pandas as pd
from datetime import datetime

from constants import FORMED_API_URL, TOMATO_TAXON_ID, LICENCES_TO_USE, BATCH_SIZE, POTATO_BLIGHT_TAXON_ID
from local_code.data_formaters import format_inaturalist_data, single_table_format_inaturalist_data

params = {
    "verifiable": "true",
    "order_by": "id",
    "order": "desc",
    "page": "1",
    "spam": "false",
    "photo_license": "cc-by",
    "photos": "true",
    "taxon_id": str(POTATO_BLIGHT_TAXON_ID),
    "locale": "en-US",
    "per_page": str(BATCH_SIZE),
    "return_bounds": "true",
}


for page_number in range(1, 3):
    current_params = params.copy()
    current_params["page"] = str(page_number)
    for licence_to_use in LICENCES_TO_USE:

        current_params["photo_license"] = licence_to_use

        response = requests.get(FORMED_API_URL, params=current_params)
        failed_licence_urls = list()
        licence_observations = list()
        failed_resource_urls = list()
        i = 0 # In cases when specific license does not have observations
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
                    print(f"Server returned status code: {curr_response.status_code} for observation {curr_id}. Setting sleep for 60 seconds...")
                    failed_resource_urls.append({"url": curr_url, "status_code": curr_response.status_code})
                    time.sleep(60)

                if i != 0 and i % BATCH_SIZE == 0:
                    # print(licence_observations) # has been uncommented
                    df_licence_observations = pd.DataFrame(licence_observations)
                    df_licence_observations.to_parquet(f'raw_data/observations_photo_batch_{page_number}_{licence_to_use}_{i}_{BATCH_SIZE}.parquet', index=False)
                    licence_observations = list()


                end_time = datetime.now()
                print(f"Step {i} execution time:", end_time - curr_start_time)

        else:
            print(f"Server returned status code: {response.status_code}! In main for loop. Sleeping for 120 seconds")
            failed_licence_urls.append({"url": FORMED_API_URL, "status_code": response.status_code}) # TODO: fix this part(add parameters) and write restoring script on file from duckdb and dbeaver
            time.sleep(120)


        df_failed_licence = pd.DataFrame(failed_licence_urls)
        df_failed_licence.to_parquet(f'raw_data/failed_licence_urls_{page_number}_{licence_to_use}.parquet', index=False)

        df_licence_observations = pd.DataFrame(licence_observations)
        df_licence_observations.to_parquet(f'raw_data/observations_photo_batch_{page_number}_{licence_to_use}_{i + 1}_{BATCH_SIZE}.parquet', index=False)

        df_failed_resource_urls = pd.DataFrame(failed_resource_urls)
        df_failed_resource_urls.to_parquet(f'raw_data/failed_resource_urls_{page_number}_{licence_to_use}.parquet', index=False)
