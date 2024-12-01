from local_code.config import DATA_DIRECTORY_PREFIX

RAW_DATA_DIR = r'C:\Users\admin\PycharmProjects\tomato dataset\local_code\raw_data'
DATA_DIRECTORY_PREFIX = DATA_DIRECTORY_PREFIX


FAILED_LICENCE_DIRECTORY = f'{RAW_DATA_DIR}\\{DATA_DIRECTORY_PREFIX}\\failed_licence'
FAILED_LICENCE_OUTPUT_PATH = \
    f'{RAW_DATA_DIR}\\initial_preprocessing\\licence_urls\\{DATA_DIRECTORY_PREFIX}_failed_licences.parquet'

FAILED_RESOURCE_DIRECTORY = f'{RAW_DATA_DIR}\\{DATA_DIRECTORY_PREFIX}\\failed_resource'
FAILED_RESOURCE_OUTPUT_PATH = \
    f'{RAW_DATA_DIR}\\initial_preprocessing\\resource_urls\\{DATA_DIRECTORY_PREFIX}_failed_resources.parquet'

OBSERVATION_DIRECTORY = f'{RAW_DATA_DIR}\\{DATA_DIRECTORY_PREFIX}\\observations'
OBSERVATION_OUTPUT_PATH = \
    f'{RAW_DATA_DIR}\\initial_preprocessing\\observation_urls\\{DATA_DIRECTORY_PREFIX}_all_observations_url.parquet'


EMPTY_LICENCE_COLUMNS = [
    'url', 'status_code'
]

OBSERVATIONS_COLUMNS = [
    'observation_id', 'time_observed_at_date', 'observed_on_date', 'observed_on_year',
    'observed_on_month', 'observed_on_week', 'observed_on_day', 'observed_on_hour',
    'location', 'place_guess', 'observed_time_zone', 'created_time_zone', 'time_zone_offset',
    'english_common_name', 'preferred_common_name', 'taxon_name', 'description',
    'identifications_most_disagree', 'identifications_most_agree',
    'quality_grade', 'uri', 'image_url', 'original_image_url', 'original_width',
    'original_height', 'license_code', 'attribution'
]

EMPTY_RESOURCE_COLUMNS = [
    'url', 'status_code'
]
