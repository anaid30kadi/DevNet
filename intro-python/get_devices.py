import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC_IP, DNAC_PORT, DNAC_USER, DNAC_PASSWORD
from DNA_Token import get_auth_token
 
def get_devices():
	token = get_auth_token() # Get a Token
	url = "https://10.1.100.10/api/v1/network-device" #Network Device endpoint
	hdr = {'x-auth-token': token, 'content-type' : 'application/json'} #Build header Info
	resp = requests.get(url, verify=False, headers=hdr)  # Make the Get Request
	device_list = resp.json() #capture the data from the controller
	print_device_list(device_list) #pretty print the data we want
    
def print_device_list(device_list):
    for device in device_list['response']:
       
   
    
if __name__ == "__main__":
    get_devices()