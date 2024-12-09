API_URL_BASE = "https://api.inaturalist.org/"
API_VERSION = "v1"
TYPE = "observations"
FORMED_API_URL = f"{API_URL_BASE}{API_VERSION}/{TYPE}"

LICENCES_TO_USE = ["cc0", "cc-by", "cc-by-nc", "cc-by-nc-sa"]
# TODO: move fully to config or use it only as descriptive field here
# TODO: Reconsider what needs to be in this file and what in configs

TOMATO_TAXON_ID = 51737
POTATO_BLIGHT_TAXON_ID = 53860
ALTERNARIA_TAXON_ID = 327996 # Early blight
SEPTORIA_TAXON_ID = 327977
TOMATO_YELLOW_CURL_VIRUS_TAXON_ID = 1555030
TOMATO_LEAF_MOLD_TAXON_ID = 1587947
TOMATO_SPIDER_MITES_TAXON_ID = 128552
TOMATO_LEAF_MINER_TAXON_ID = 48086
BATCH_SIZE = 200

# Below params were used as an initializer
number_of_params = [
    {
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
    },
    {
        "verifiable": "true",
        "order_by": "id",
        "order": "desc",
        "page": "1",
        "spam": "false",
        "photo_license": "cc-by",
        "photos": "true",
        "taxon_id": str(TOMATO_TAXON_ID),
        "locale": "en-US",
        "per_page": str(BATCH_SIZE),
        "return_bounds": "true",
    },
    {
        "verifiable": "true",
        "order_by": "id",
        "order": "desc",
        "page": "1",
        "spam": "false",
        "photo_license": "cc-by",
        "photos": "true",
        "taxon_id": str(ALTERNARIA_TAXON_ID),
        "locale": "en-US",
        "per_page": str(BATCH_SIZE),
        "return_bounds": "true",
        "q": "tomato"
    },
    {
        "verifiable": "true",
        "order_by": "id",
        "order": "desc",
        "page": "1",
        "spam": "false",
        "photo_license": "cc-by",
        "photos": "true",
        "taxon_id": str(SEPTORIA_TAXON_ID),
        "locale": "en-US",
        "per_page": str(BATCH_SIZE),
        "return_bounds": "true",
        "q": "tomato"
    },
    {
        "verifiable": "true",
        "order_by": "id",
        "order": "desc",
        "page": "1",
        "spam": "false",
        "photo_license": "cc-by",
        "photos": "true",
        "taxon_id": str(TOMATO_YELLOW_CURL_VIRUS_TAXON_ID),
        "locale": "en-US",
        "per_page": str(BATCH_SIZE),
        "return_bounds": "true",
        "q": "tomato"
    },
    {
        "verifiable": "true",
        "order_by": "id",
        "order": "desc",
        "page": "1",
        "spam": "false",
        "photo_license": "cc-by",
        "photos": "true",
        "taxon_id": str(TOMATO_LEAF_MOLD_TAXON_ID),
        "locale": "en-US",
        "per_page": str(BATCH_SIZE),
        "return_bounds": "true"
    },
]
