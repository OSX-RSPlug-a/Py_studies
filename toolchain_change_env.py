from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cd_toolchain_v2 import CdToolchainV2
import os


API_KEY = "YOUR_IBM_CLOUD_API_KEY"
authenticator = IAMAuthenticator(API_KEY)
toolchain_service = CdToolchainV2(authenticator=authenticator)
toolchain_service.set_service_url("https://api.control.devops.cloud.ibm.com")


ENV_VAR_NAME = "TARGET_ENV_VAR"
NEW_VALUE = "new-value"
REGION = "us-south"


try:
    toolchains = toolchain_service.list_toolchains(region=REGION).get_result()
    
    for toolchain in toolchains['toolchains']:
        toolchain_id = toolchain['id']
        print(f"Updating toolchain: {toolchain['name']} ({toolchain_id})")
        
        
        toolchain_service.update_toolchain(
            toolchain_id=toolchain_id,
            env={ENV_VAR_NAME: NEW_VALUE}
        )
        print(f"Updated {ENV_VAR_NAME} to {NEW_VALUE}")

except Exception as e:
    print(f"Error: {e}")


# https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-toolchains-iam-security
# https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-toolchains_getting_started&interface=ui
# https://cloud.ibm.com/docs/codeengine?topic=codeengine-envvar