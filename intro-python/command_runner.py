import requests
import json
from DNA_Token import get_auth_token

def get_device():
    """Building out function to retrieve the uuid of a device. Using requests.get to make a call to the network device"""
    token = get_auth_token() # Get Token
    url = "https://10.1.100.9/dna/intent/api/v1/network-device/ip-address/10.1.255.10"
    hdr = {'x-auth-token': token, 'content-type' : 'application/json'}
    resp = requests.get(url, verify=False, headers=hdr)  # Make the Get Request
    device_det = resp.json()
    post_commandr_list(device_det, token)

def post_commandr_list(device_inf_json, post_token):
    """Building out function to retrieve list of command runner commands. Using requests.get to make a call to the DNAC"""
    device_uuid = device_inf_json['response']['id']
    print ("The device id is:",device_uuid)
    post_token = get_auth_token() # Get Token
    url = "https://10.1.100.9/dna/intent/api/v1/network-device-poller/cli/read-request"
    hdr = {'x-auth-token': post_token, 'content-type' : 'application/json'}
    param = {
        "name" : "show ver",
        "commands" : ["show clock"],
        "deviceUuids" : [device_uuid]
        }
    resp = requests.post(url, verify=False, headers=hdr, data=json.dumps(param))  # Make the Post
    command_show = resp.json()
    print (command_show)
     
if __name__ == "__main__":
    get_device()