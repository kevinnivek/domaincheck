#!/usr/bin/python
# This script takes a list of IP addrseses and parses the whois data using IPWhois 
# to produce the current hosting provider

import sys
import socket
import json
from urlparse import urlparse
from ipwhois import IPWhois
from pprint import pprint

file = open( 'output.txt', 'w')
with open( 'input.txt' ) as f:
    for line in f:
         obj = IPWhois(line.strip())
         results = obj.lookup()
         encoded_str = json.dumps( results )
         decoded_data = json.loads( encoded_str )
         name = decoded_data['nets'][0]['name']
         desc = decoded_data["nets"][0]["description"]
         emad = decoded_data["nets"][0]["abuse_emails"]
         print 'name : ' + name + ' description : ' + desc + ' abuse email : ' + emad
         file.write(name + ',' + desc + ',' + emad + '\n')

file.close()



