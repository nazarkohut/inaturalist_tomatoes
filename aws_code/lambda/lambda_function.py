import json
import requests
from datetime import datetime

from data_formaters import format_inaturalist_data

API_URL_BASE = "https://api.inaturalist.org/"
API_VERSION = "v1"
TYPE = "observations"
FORMED_API_URL = f"{API_URL_BASE}{API_VERSION}/{TYPE}"

def inaturalist_date_retriever(event, context):
    params = event.copy()

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
                return  {
                    'statusCode': 200,
                    'body': json.dumps(formated_data[0])
                }
            else:
                return  {
                    'statusCode': 429,
                    'body': json.dumps(formated_data[0])
                }
                print(f"Server returned status code: {curr_response.status_code} for observation {curr_id}")
    else:
        print(f"Server returned status code: {response.status_code}! In main for loop.")
    return {
        'statusCode': 500,
        'body': {"message": "Somewhy previous returns did not work as expected"}
    }
