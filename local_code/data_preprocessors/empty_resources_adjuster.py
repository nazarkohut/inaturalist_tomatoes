from local_code.data_preprocessors.miscs.preprocessors import process_parquet_files

# directory = r'C:\Users\admin\PycharmProjects\tomato dataset\local_code\raw_data\tomatoes_data\failed_resource'
# output_path = r'C:\Users\admin\PycharmProjects\tomato dataset\local_code\raw_data\initial_preprocessing\resource_urls\tomatoes_data_failed_resources.parquet'

directory = r'C:\Users\admin\PycharmProjects\tomato dataset\local_code\raw_data\potato_blight\failed_resource'
output_path = r'C:\Users\admin\PycharmProjects\tomato dataset\local_code\raw_data\initial_preprocessing\resource_urls\potato_light_failed_resources.parquet'


columns = [
    'url', 'status_code'
]

process_parquet_files(directory, output_path, columns, filename_prefix="failed_resource_")