__author__ = 'citlalig'

import ckanapi

class CkanDatosAbiertosMX:

    def __init__(self, site_name, user_agent=None):
        self.cknsite = ckanapi.RemoteCKAN(site_name,
        user_agent= user_agent)

    def getOrganizationList(self):
        # Return a list of the names of the site organizations.
        return self.cknsite.action.organization_list()

    def getOrganizationDetails(self, org):
        # Return the details of a organization
        return self.cknsite.action.organization_show(id=org)

    def getPackageList(self):
        # Return a list of the names of the site datasets (packages).
        return self.cknsite.action.package_list()

    def getPackageDetails(self, pck):
        #Return the metadata of a dataset (package) and its resources.
        return self.cknsite.action.package_show(id=pck)

    def getTagList (self):
        #Return a list of the site tags.
        return self.cknsite.action.tag_list()

    def getTagDetails(self, tag):
        #Return the details of a tag and all its datasets.
        return self.cknsite.action.show_tag(id=tag)

    def getResourceDetails(self, rsrc):
        #Return the metadata of a resource.
        return self.cknsite.action.resource_show(id=rsrc)





