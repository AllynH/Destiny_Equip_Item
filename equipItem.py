###################################################################################################
# Introduction:	This program takes an item from a characters Vault, transfers the item the the characters inventory and equips the item.
#				For more details view the full blog post: http://allynh.com/blog/creating-a-python-app-for-destiny-part-4-transferring-and-equipping-items
#				For details on how to log into PSN view this blog post: http://allynh.com/blog/creating-a-python-app-for-destiny-part-3-logging-in-to-bungie-net-and-authenticating-with-psn/
#
# Notes:		This code will require you to update:
#					Your PSN log in details
#					Your Bungie.net API-Key
#					Your characterId and the item details - I've left mine in as an example.
#				Please read the blog post for more information
#
# Usage:		python equipItem.py
# Created by:	Allyn Hunt - www.AllynH.com
###################################################################################################

from PSN_login import login
import requests
import json

# Uncomment this line to print JSON output to a file:
#f = open('output.txt', 'w')

# PSN log in details and Bungie.net API-KEY:
username = emailaddr
password = mypassword
api_key = API_KEY

# Log in via PSN and create our persistant HTTP session: 
session = requests.Session()
session = login(username, password, api_key)

# Build the transfer item payload:
text_payload = {
	"membershipType": 2,
	"itemReferenceHash": 1519376148,	# The Ram
	"itemId": 6917529085991104887,		# The Ram
	"characterId": characterId_Warlock,
	"stackSize": 1,
	"transferToVault": False
}
payload = json.dumps(text_payload)

# Send the request to transfer the item:
req_string = base_url + "TransferItem/"
print "Transferring item from vault to character..."
res = session.post(req_string, data=payload)
error_stat = res.json()['ErrorStatus'].decode('utf-8')
print "Error status: " + error_stat + "\n"

# Build the equip item payload:
text_equip_payload = {
	"membershipType": 2,
	"itemId": 6917529085991104887,		# The Ram
	"characterId": characterId_Warlock
}
equip_payload = json.dumps(text_equip_payload)

# Send the request to equip the item:
equip_url = base_url + "EquipItem/"
print "Equipping item..."
res = session.post(equip_url, data=equip_payload)
error_stat = res.json()['ErrorStatus'].decode('utf-8')
print "Error status: " + error_stat + "\n"

# Uncomment this line to print JSON output to a file:
#f.write (json.dumps(res.json(), indent=4))
