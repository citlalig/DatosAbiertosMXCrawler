# Encoding: UTF-8
__author__ = 'citlalig'

from ckandgm import CkanDatosAbiertosMX
import urllib2
import os
import httplib
import socket
import ssl
import sys

def writeFile(fileName, data):
    output = open(fileName, 'wb')
    output.write(data)
    output.close()

def downloadFile(url, path, resource_name, resource_format, space=""):
    print space + 'Downloading file '+ url
    try:
        response = urllib2.urlopen(url, timeout = 30)
        if resource_format == "" :
            basename = os.path.basename(url)
            resource_format = basename[basename.rfind('.')+1:]
        file_name = resource_name + '.' + resource_format.lower()
        file_name.encode("UTF-8")
        print space + 'Save file ' + file_name + ' to Path: ' + path
        complete_file_name = os.path.join(path, file_name)
        writeFile(complete_file_name, response.read())

    except urllib2.HTTPError, e:
        print type(e)
    except httplib.BadStatusLine, e:
        print type(e)
    except urllib2.URLError, e:
        print type(e)
    except socket.timeout as e:
        print type(e)
    except ssl.SSLError as e:
        print type(e)
    except ssl.SSLError as e:
        print type(e)
    except IOError as e:
        print type(e)
    except:
        print 'An exception occurred'

def makeDir(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)

##### MAIN CODE ####

SITE_NAME = 'http://catalogo.datos.gob.mx/'
USER_AGENT = 'MXOpenDataEngine/1.0'
organizations_list = ['pemex', 'promexico', 'sep', 'presidencia', 'sagarpa', 'shcp', 'sedesol' ]
MAIN_FOLDER = 'catalogo'
SHOW_DETAILS_ACTION = 'api/3/action/organization_show?id='
datosabiertosmx = CkanDatosAbiertosMX(SITE_NAME, USER_AGENT)
makeDir(MAIN_FOLDER)
organizations = datosabiertosmx.getOrganizationList()
for org in organizations:
    print "Organization: ", org
    if org in organizations_list:
        print "Processing Organization: " + org
        org_det = datosabiertosmx.getOrganizationDetails(org)
        name = org_det['name']
        path = os.path.join(MAIN_FOLDER, name)
        makeDir(path)
        downloadFile(SITE_NAME + SHOW_DETAILS_ACTION + name, path, name, "json")
        packages = org_det['packages']
        for package in packages:
            package_name = package['name']
            print '\tProcessing Package: "' + package_name
            path = os.path.join(os.path.join(MAIN_FOLDER , name , package_name))
            makeDir(path)
            resources = package['resources']
            for resource in resources:
                print '\t\tProcessing Resource '+ resource['name']
                downloadFile(resource['url'], path, resource['name'], resource['format'], "\t\t")