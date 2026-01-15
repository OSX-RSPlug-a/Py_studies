import json
import os
import sys
from ibm_code_engine_sdk.code_engine_v2 import *
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#pip install ibm-code-engine-sdk
#pip install ibm_cloud_sdk_core


PROJECT_ID = 'your-project-guid-here'
JOB_RUN_NAME = 'my-job-run-xyz'
APP_NAME = 'my-app'
APP_KEY = 'my-app-key'

authenticator = IAMAuthenticator(API_KEY)
ce_service = CodeEngineV2(authenticator=authenticator)
ce_service.set_service_url('https://api.us-south.codeengine.cloud.ibm.com/v2')


try:
    response = ce_service.get_app_logs(
        project_id=PROJECT_ID,
        name=APP_NAME
        )
    
    print("--- Job Run Logs ---")
    print(response.get_result())
    
    
except Exception as e:
    print(f"Failed to fetch logs: {e}")