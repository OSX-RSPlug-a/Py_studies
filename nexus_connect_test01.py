import requests
import base64


NEXUS_URL = "<http://your_nexus_host:8081>"
TOKEN_NAME = "<your_nexus_token_name_or_id>"
TOKEN_PASSCODE = "your_nexus_token_passcode_Token"

def check_nexus_connection_with_token(nexus_url, token_name, token_passcode):
    try:
        auth_string = f"{token_name}:{token_passcode}"
        encoded_auth = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')

        headers = {
            "Authorization": f"Basic {encoded_auth}",
            "Accept": "application/json"
        }

        status_endpoint = f"{nexus_url}/service/rest/v1/status"

        print(f"Attempting to connect to Nexus at: {status_endpoint}")
        response = requests.get(status_endpoint, headers=headers, timeout=10)

        if response.status_code == 200:
            print("Successfully connected to Nexus by token!")
            print("Nexus status:")
            print(response.json())
            return True
        else:
            print(f"Failed to connect. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: {nexus_url}. Error: {e}")
        return False
    except requests.exceptions.Timeout as e:
        print(f"Timeout Error: Request to Nexus at {nexus_url} . Error: {e}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred: {e}")
        return False
    except Exception as e:
        print(f"An unknown error occurred: {e}")
        return False

if __name__ == "__main__":
    if check_nexus_connection_with_token(NEXUS_URL, TOKEN_NAME, TOKEN_PASSCODE):
        print("\nNexus connection check Successfully.")
    else:
        print("\nNexus connection check failed.")

    # You could also try to list repositories as a more functional check
    # if you have the appropriate permissions with your token.
    # For example:
    # REPOSITORIES_ENDPOINT = f"{NEXUS_URL}/service/rest/v1/repositories"
    # response = requests.get(REPOSITORIES_ENDPOINT, headers=headers)
    # if response.status_code == 200:
    #     print("\nSuccessfully fetched repositories:")
    #     print(response.json())
    # else:
    #     print(f"\nFailed to fetch repositories. Status code: {response.status_code}")
