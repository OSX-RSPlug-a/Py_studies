import os
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import get_authenticator_authenticator
from ibm_platform_services import ResourceControllerV2
from ibm_continuous_delivery import ContinuousDeliveryV1


API_KEY = "YOUR_IBM_CLOUD_API_KEY"
RESOURCE_GROUP_NAME = "YOUR_RESOURCE_GROUP_NAME"
NEW_ENV_VAR_NAME = "YOUR_VARIABLE_NAME"
VAULT_SECRET_NAME = "YOUR_SECRET_NAME"

REGION = "us-south" 

authenticator = IAMAuthenticator(API_KEY)


resource_controller_service = ResourceControllerV2(authenticator=authenticator)
resource_controller_service.set_service_url(f"https://resource-controller.cloud.ibm.com")


cd_service = ContinuousDeliveryV1(authenticator=authenticator)

cd_service.set_service_url(f"https://api.{REGION}.continuousdelivery.cloud.ibm.com") 


def get_secret_from_vault(secret_name):

    print(f"Retrieving secret '{secret_name}' from the vault...")
    
    return "THE_NEW_SECRET_VALUE" 


new_value = get_secret_from_vault(VAULT_SECRET_NAME)


resource_group_id = None

try:
    resource_groups = resource_controller_service.list_resource_groups().get_result()
    for group in resource_groups.get('resources'):
        if group['name'] == RESOURCE_GROUP_NAME:
            resource_group_id = group['id']
            break
        
except Exception as e:
    print(f"Error retrieving resource groups: {e}")

if not resource_group_id:
    print(f"Resource group '{RESOURCE_GROUP_NAME}' not found.")
else:
    print(f"Found Resource Group ID: {resource_group_id}")
    toolchains = []
    
    try:
        toolchains_list = cd_service.list_toolchains(resource_group_id=resource_group_id).get_result()
        toolchains = toolchains_list.get('toolchains', [])
    except Exception as e:
        print(f"Error retrieving toolchains: {e}")

    if not toolchains:
        print(f"No toolchains found in resource group '{RESOURCE_GROUP_NAME}'.")
    else:
        for toolchain in toolchains:
            toolchain_id = toolchain['id']
            toolchain_name = toolchain['name']
            print(f"Updating toolchain: {toolchain_name} ({toolchain_id})")

            try:
                print(f"Manually proceed to the IBM Cloud console for toolchain {toolchain_name} to update the pipeline environment property: {NEW_ENV_VAR_NAME}.")
                

            except Exception as e:
                print(f"Failed to update toolchain {toolchain_name}: {e}")

