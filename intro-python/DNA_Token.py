import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC_IP, DNAC_PORT, DNAC_USER, DNAC_PASSWORD

def get_auth_token():
    """Building out Auth request. Using requests.post to make a call to the Auth Endpoint"""
    url = 'https://10.1.100.10/dna/system/api/v1/auth/token'       # Endpoint URL
    resp = requests.post(url, verify=False, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD))  # Make the POST Request
    token = resp.json()['Token']    # Retrieve the Token from the returned JSON
    #print("Token Retrieved: {}".format(token))  # Print out the Token
    return token
	
if __name__ == "__main__":
 get_auth_token()