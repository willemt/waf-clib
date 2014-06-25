from waflib.Configure import conf

import simplejson as json
import os


@conf
def clib_info(self, package):
    path = "%s/deps/%s/" % (os.getcwd(), package)
    json_data = open("%s/package.json" % (path))
    data = json.load(json_data)
    json_data.close()
    return data


@conf
def clib_h_files(self, package):
    return filter(lambda x: x.endswith(".h"), self.clib_info(package)['src'])


@conf
def clib_c_files(self, package):
    return filter(lambda x: x.endswith(".c"), self.clib_info(package)['src'])
