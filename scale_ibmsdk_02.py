import os
import requests
import json
import time
from ibmcloud_python_sdk.power import instance_ids
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Authenticate with API-KEY and get Bearer Token
#url = "https://iam.cloud.ibm.com/identity/token"

headers = {
	"Content-Type": "application/x-www-form-urlencoded",
	"Accept": "application/json",
	}
#API_KEY = os.environ['api_key']
#data = [
#        ("grant_type", "urn:ibm:params:oauth:grant-type:apikey"),
#        ("apikey", API_KEY),
#]
#auth_response = requests.request("POST", url, headers=headers, data=data)
# Create Bearer Auth string
#auth_token = 'Bearer ' + auth_response.json()['access_token']
# Now you can use "'Authorization': auth_token," on requests

headers = {
	#'Authorization': auth_token,
	'CRN': os.getenv('CRN'),
	'Content-Type': 'application/json',
	}


API_KEY = os.environ['api_key']
authenticator = IAMAuthenticator(API_KEY)
service = instance_ids(authenticator=authenticator)

# Set MEM/CPU data
json_data_cpu = {
        'processors': float(os.environ['CPU']),
	}
json_data_memory = {
        'memory': float(os.environ['MEMORY']),
        }
# Create empty instance ID list
instance_ids = []

# Fill instance ID list from ENV variables
for INST in range(1,100):
	try:
		instance_ids.append(os.environ['INST_' + str(INST)])
	except:
		break

# Create response variable so it can be used in condition before requests
#response = auth_response​

for instance_id in instance_ids:
        # Set status for while loop
        status = True
        # Change status code of response to anything but 202 (sucessful)
        response.status_code = 400
        while status:
                if (response.status_code != 202):
                        time.sleep(10)
                        response = requests.put(
                                os.getenv('ENDPOINT') + '/pcloud/v1/cloud-instances/' + os.getenv('CLOUD_INSTANCE_ID') + '/pvm-instances/' + instance_id,
                                headers=headers,
                                json=json_data_cpu,
                        )
                else:
                        status = False

# Add wait time in between CPU & MEM
time.sleep(10)


for instance_id in instance_ids:
        # Set status for while loop
        status = True
        # Change status code of response to anything but 202 (sucessful)
        response.status_code = 400
        while status:
                if (response.status_code != 202):
                        time.sleep(10)
                        response = requests.put(
                                os.getenv('ENDPOINT') + '/pcloud/v1/cloud-instances/' + os.getenv('CLOUD_INSTANCE_ID') + '/pvm-instances/' + instance_id,
                                headers=headers,
                                json=json_data_memory,
                                )
                else:
                        status = False


# ibmcloud ce project create -n Project_scale_powervsi
# ibmcloud ce project select -n Project_scale_powervsi
# ibmcloud ce secret create --name api-key --from-literal api_key=<your-api-token>
# ibmcloud ce job create --name action-scale --build-source . --wait --cpu .125 --memory .25G --env-from-secret api-key
