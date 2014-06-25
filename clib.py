from waflib.Configure import conf

import simplejson as json
import os


@conf
def clib_info(self, package):
    json_data = open("%s/package.json" % (self.clib_path(package)))
    data = json.load(json_data)
    json_data.close()
    return data


@conf
def clib_h_files(self, package):
    return filter(lambda x: x.endswith(".h"), self.clib_info(package)['src'])


@conf
def clib_c_files(self, package):
    return filter(lambda x: x.endswith(".c"), self.clib_info(package)['src'])


@conf
def clib_c_file(self, package):
    """ Return one c file.
        This is for packages where we only expect one c file """
    return self.clib_c_files[0]


@conf
def clib_h_file(self, package):
    """ Return one h file.
        This is for packages where we only expect one c file """
    return self.clib_h_files[0]


@conf
def clib_path(self, package):
    return "%s/deps/%s/" % (os.getcwd(), package)
