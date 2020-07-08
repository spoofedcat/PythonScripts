#!/usr/bin/env python
# 08:00:27:fd:a9:10
# raw_input for python 2.7
# input for python 3

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (values, arguments) = parser.parse_args()

    if not values.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not values.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return values

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


values = get_arguments()
current_mac = get_current_mac(values.interface)

print("Current MAC = " + str(current_mac))

change_mac(values.interface, values.new_mac)

current_mac = get_current_mac(values.interface)

if current_mac == values.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed.")
