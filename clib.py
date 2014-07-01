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
def clib_h_files(self, package, included_deps=True):
    """ Get all header files for a package.
        By default, aslo get the package's dependency source files too """
    return filter(lambda x: x.endswith(".h"), self.clib_info(package)['src'])


@conf
def clib_c_files(self, package, included_deps=True):
    """ Get all c files for a package.
        By default, aslo get the package's dependency source files too """
    return filter(lambda x: x.endswith(".c"), self.clib_info(package)['src'])


@conf
def clib_c_file(self, package):
    """ Return one c file.
        This is for packages where we only expect one c file """
    files = self.clib_c_files(package)
    if 0 < len(files):
        raise Exception('Expected only one source file')
    return files[0]


@conf
def clib_h_file(self, package):
    """ Return one h file.
        This is for packages where we only expect one c file """
    files = self.clib_h_files(package)
    if 0 < len(files):
        raise Exception('Expected only one source file')
    return files[0]


@conf
def clib_path(self, package):
    return "%s/deps/%s/" % (os.getcwd(), package)
