import requests
import pandas as pd
from datetime import datetime

from constants import FORMED_API_URL, TOMATO_TAXON_ID, LICENCES_TO_USE
from local_code.data_formaters import format_inaturalist_data


params = {
    "verifiable": "true",
    "order_by": "id",
    "order": "desc",
    "page": "1",
    "spam": "false",
    "photo_license": "cc-by",
    "photos": "true",
    "taxon_id": str(TOMATO_TAXON_ID),
    "locale": "en-US",
    "per_page": "5",
    "return_bounds": "true",
}


for licence_to_use in LICENCES_TO_USE:
    current_params = params.copy()
    current_params["photo_license"] = licence_to_use

    response = requests.get(FORMED_API_URL, params=params)

    if response.status_code == 200:
        for i, curr_res in enumerate(response.json()['results']):
            curr_start_time = datetime.now()
            curr_id = curr_res['id']

            curr_url = f"{FORMED_API_URL}/{curr_id}?include_new_projects=true&preferred_place_id=&locale=en-US&ttl=-1"
            curr_response = requests.get(curr_url)

            if curr_response.status_code == 200:
                result_data = curr_response.json()['results']
                formated_data = format_inaturalist_data(result_data, curr_id)

                print(f"Formatted inaturalist data for observation {curr_id}")
                print(formated_data)
            else:
                print(f"Server returned status code: {curr_response.status_code} for observation {curr_id}. Setting sleep for 30 seconds...")



            end_time = datetime.now()
            print(f"Step {i} execution time:", end_time - curr_start_time)

    else:
        print(f"Server returned status code: {response.status_code}! In main for loop.")

