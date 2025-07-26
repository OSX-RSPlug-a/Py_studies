import requests

resp = requests.get(
    "https://theverge.com/")
    
if resp.status_code == 200:
    print("Status: Success, Ok and Online")
if resp.status_code == 301:
    print("Status: Permanent Redirect. The page you have requested has moved to a new URL and which is permanent.")
if resp.status_code == 302:
    print("Status: Temporary Redirect. The redirection is temporarily redirected to another website.")
if resp.status_code == 304:
    print("Status: Not Modified. The response has not been changed.")
if resp.status_code == 400:
    print("Status: Bad Request. Not online")
if resp.status_code == 401:
    print("Status: Unauthorized Error. Basic and Digest Access Authentication.")
if resp.status_code == 403:
    print("Status: Forbidden. The request is understood by the server, but still refuses to fulfill it.")
if resp.status_code == 404:
    print("Status: Page Not Found. The server is not able to find a representation for the target resource.")
if resp.status_code == 500:
    print("Status: Internal Server Error. There's an error during a connection to the server.")
if resp.status_code == 501:
    print("Status: Not Implemented. The server does not support the functionality required to fulfill the request.")
else:
    print(f"It got another http status: {resp.status_code}")
