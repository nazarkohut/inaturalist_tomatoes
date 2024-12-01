from constants import TOMATO_LEAF_MINER_TAXON_ID

DATA_DIRECTORY_PREFIX = "tomato_leaf_miner"
BASE_PREFIX_DIR = f"raw_data/{DATA_DIRECTORY_PREFIX}"

CURRENT_TAXON_ID = TOMATO_LEAF_MINER_TAXON_ID

USE_QUERY_PARAM = True
CURRENT_QUERY_PARAM = "tomato"


# Values used in for loop, might change in the future to automatically adjusted based on number of found items
LOWER_BOUND = 1
UPPER_BOUND = 2

# Set time sleep periods in between requests
FAILED_RESOURCE_TIME_SLEEP = 60
FAILED_LICENCE_TIME_SLEEP = 120
