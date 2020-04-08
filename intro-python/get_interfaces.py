import requests
from dnac_config import DNAC_IP, DNAC_PORT, DNAC_USER, DNAC_PASSWORD
from DNA_Token import get_auth_token


def get_device_list():
    """Building out function to retrieve list of devices. Using requests.get to make a call to the network device Endpoint"""
    token = get_auth_token() # Get Token
    url = "https://10.1.100.10/api/v1/network-device"
    hdr = {'x-auth-token': token, 'content-type' : 'application/json'}
    resp = requests.get(url, verify=False, headers=hdr)  # Make the Get Request
    device_list = resp.json()
    get_device_int(device_list, token)
    
def get_all_int(int_token):
  """Building out function to retrieve device interface. Using requests.get to make a call to the network device Endpoint"""
  url = "https://10.1.100.10/api/v1/interface"
  hdr = {'x-auth-token': int_token, 'content-type' : 'application/json'}
  querystring = {'limit': 5}
  resp = requests.get(url, verify=False, headers=hdr, params=querystring)  # Make the Get Request 
  interface_info_json = resp.json()
  print_interface_info(interface_info_json)

def get_device_int(device_list, token):
  for device in device_list['response']:
    device_id = device['id']
    print ("The device id is:", device_id)
    url = "https://10.1.100.10/api/v1/interface/network-device/{}".format(device_id)
    hdr = {'x-auth-token': token, 'content-type' : 'application/json'}
    resp = requests.get(url, verify=False, headers=hdr)  # Make the Get Request 
    interface_info_json = resp.json()
    if resp.status_code == 200:
        print_interface_info(interface_info_json)
    else:
        print ("Este dispositivo no contiene interfaces")
    
def print_interface_info(interface_list):
  print("{0:30}{1:17}{2:12}{3:30}{4:12}{5:16}{6:15}".format("PortName", "VlanID", "PortMode", "PortType", "Duplex", "Status", "LastUpdated"))
  for interface in interface_list['response']:
    Name = interface['portName']
    Vlan = interface['vlanId']
    Mode = interface['portMode']
    Type = interface['portType']
    status = interface['status']
    updated = interface['lastUpdated']
    if interface['duplex'] is None:
        duplex = "None"
    else:
        duplex = interface['duplex']
    print("{0:30}{1:17}{2:12}{3:30}{4:12}{5:16}{6:15}".format(Name, Vlan, Mode, Type, duplex, status, updated))


if __name__ == "__main__":
    get_device_list()
    