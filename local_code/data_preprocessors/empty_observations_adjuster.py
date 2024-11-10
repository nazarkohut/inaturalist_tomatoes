from local_code.data_preprocessors.miscs.preprocessors import process_parquet_files

# TODO: test this part out with new data
directory = r'C:\Users\admin\PycharmProjects\tomato dataset\local_code\raw_data\tomatoes_data'
output_path = r'../raw_data/initial_preprocessing/observation_urls/tomatoes_data_all_observations_urls.parquet'
columns = [
    'observation_id', 'time_observed_at_date', 'observed_on_date', 'observed_on_year',
    'observed_on_month', 'observed_on_week', 'observed_on_day', 'observed_on_hour',
    'location', 'place_guess', 'observed_time_zone', 'created_time_zone', 'time_zone_offset',
    'english_common_name', 'preferred_common_name', 'taxon_name', 'description',
    'identifications_most_disagree', 'identifications_most_agree',
    'quality_grade', 'uri', 'image_url', 'original_image_url', 'original_width',
    'original_height', 'license_code', 'attribution'
]

process_parquet_files(directory, output_path, columns)

