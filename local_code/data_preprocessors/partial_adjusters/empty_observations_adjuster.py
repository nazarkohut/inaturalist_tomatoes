from local_code.data_preprocessors.config import OBSERVATIONS_COLUMNS
from local_code.data_preprocessors.miscs.preprocessors import process_parquet_files

directory = r'C:\Users\admin\PycharmProjects\tomato dataset\local_code\raw_data\tomatoes_data'
output_path = r'../../raw_data/initial_preprocessing/observation_urls/tomatoes_data_all_observations_urls.parquet'


if __name__ == "__main__":
    process_parquet_files(directory, output_path, OBSERVATIONS_COLUMNS)

