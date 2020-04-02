#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""


import json
import os


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

# TODO: Parse the contents of the JSON file into a variable
with open(os.path.join(here, "interfaces.json")) as file:
    json_file = file.read()
    json_data = json.loads(json_file)
    
# TODO: Loop through the interfaces in the JSON data and print out each interface's name, ip, and netmask.
for interface in json_data["ietf-interfaces:interfaces"]["interface"]:
    name = interface["name"]
    ip = interface["ietf-ip:ipv4"]["address"][0]["ip"]
    mask = interface["ietf-ip:ipv4"]["address"][0]["netmask"]
    print ("Your interface name is: {name}, your ip address is: {ip} and your netmask is: {mask}".format(name=name, ip=ip, mask=mask))
