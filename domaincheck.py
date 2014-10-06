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
file2 = open( 'output2.txt', 'w')
with open( 'input.txt' ) as f:
    for line in f:
         parsed_uri = urlparse(line.strip())
         domain = '{uri.netloc}'.format(uri=parsed_uri)
         addr = socket.gethostbyname(domain)
         obj = IPWhois(addr.strip())
         results = obj.lookup()
         encoded_str = json.dumps( results )
         decoded_data = json.loads( encoded_str )
         name = decoded_data['nets'][0]['name'].replace('\n', '')
         desc = decoded_data["nets"][0]["description"].replace('\n', '')
         emad = decoded_data["nets"][0]["abuse_emails"].replace('\n', ' ')
         print 'domain : ' + domain + ' name : ' + name + ' description : ' + desc + ' abuse email : ' + emad
         file.write(name + ',' + desc + ',' + emad + '\n')
         file2.write(addr + '\n')

file.close()
file2.close()



