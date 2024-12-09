# Your metadata file and Roboflow API key
from local_code.roboflow.upload_config import ROBOFLOW_PROJECT_CONFIG, ROBOFLOW_ACCOUNT_EMAIL

API_KEY = ROBOFLOW_PROJECT_CONFIG[ROBOFLOW_ACCOUNT_EMAIL]["API_KEY"]
WORKSPACE_ID = ROBOFLOW_PROJECT_CONFIG[ROBOFLOW_ACCOUNT_EMAIL]["workspaceId"]
PROJECT_ID = ROBOFLOW_PROJECT_CONFIG[ROBOFLOW_ACCOUNT_EMAIL]["projectId"]