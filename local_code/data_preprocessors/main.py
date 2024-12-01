from local_code.data_preprocessors.config import (
    EMPTY_RESOURCE_COLUMNS, FAILED_RESOURCE_DIRECTORY, \
    FAILED_RESOURCE_OUTPUT_PATH, OBSERVATIONS_COLUMNS, \
    OBSERVATION_OUTPUT_PATH, OBSERVATION_DIRECTORY, \
    EMPTY_LICENCE_COLUMNS, FAILED_LICENCE_DIRECTORY, FAILED_LICENCE_OUTPUT_PATH
)
from local_code.data_preprocessors.miscs.preprocessors import process_parquet_files

process_parquet_files(
    FAILED_LICENCE_DIRECTORY,
    FAILED_LICENCE_OUTPUT_PATH,
    EMPTY_LICENCE_COLUMNS,
    filename_prefix="failed_licence_"
)

process_parquet_files(
    OBSERVATION_DIRECTORY,
    OBSERVATION_OUTPUT_PATH,
    OBSERVATIONS_COLUMNS
)

process_parquet_files(
    FAILED_RESOURCE_DIRECTORY,
    FAILED_RESOURCE_OUTPUT_PATH,
    EMPTY_RESOURCE_COLUMNS,
    filename_prefix="failed_resource_"
)
