import os
import json

here = os.getcwd()
with open(os.path.join(here, "interfaces.json")) as file:
    json_text = file.read()

json_data = json.loads(json_text)

print("")
for i in json_data["ietf-interfaces:interfaces"]["interface"]:
    print("{} {} {}".format(i["name"], i["ietf-ip:ipv4"]["address"][0]["ip"], i["ietf-ip:ipv4"]["address"][0]["netmask"]))

print("")
##!!!
#will print this

#GigabitEthernet1 198.18.134.11 255.255.192.0
#GigabitEthernet2 172.16.255.1 255.255.255.0
##Loopback0 10.0.0.1 255.255.255.255
#!!!



