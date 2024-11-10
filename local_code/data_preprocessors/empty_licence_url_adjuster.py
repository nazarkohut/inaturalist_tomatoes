from local_code.data_preprocessors.miscs.preprocessors import process_parquet_files

# directory = r'C:\Users\admin\PycharmProjects\tomato dataset\local_code\raw_data\tomatoes_data\failed_licence'
# output_path = r'/local_code/raw_data/initial_preprocessing/licence_urls/tomatoes_data_failed_licences.parquet'

directory = r'C:\Users\admin\PycharmProjects\tomato dataset\local_code\raw_data\potato_blight\failed_licence'
output_path = r'C:\Users\admin\PycharmProjects\tomato dataset\local_code\raw_data\initial_preprocessing\licence_urls\potato_blight_failed_licences.parquet'

columns = [
    'url', 'status_code'
]

process_parquet_files(directory, output_path, columns, filename_prefix="failed_licence_")