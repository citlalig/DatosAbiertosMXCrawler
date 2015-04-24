__author__ = 'citlalig'


import urllib2
import json
import pprint

SITE_NAME = 'http://catalogo.datos.gob.mx'
API_VERSION = '/api/3'
GROUP_LIST_ACTION = '/action/group_list'
PACKAGE_LIST_ACTION = '/action/package_list'

# Make the HTTP request.
response = urllib2.urlopen()

assert response.code == 200

# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read())

# Check the contents of the response.
assert response_dict['success'] is True
result = response_dict['result']
pprint.pprint(result)