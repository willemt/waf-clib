What?
-----
A WAF tool that makes interaction with installed clib packages much easier.

How does it work?
-----------------

1. Install your favourite clib package::
    
    clib install strndup

2. Add clib.py to the same folder as your waf file (note: your deps folder is expected to be in the same folder as your waf file)

3. Inside wscript you can access aspects of clib packages using the following methods::

    def configure(conf):
        conf.load('clib') # load clib tool
        print conf.clib_c_files('strndup') # list all c files for strndup
        print conf.clib_h_files('strndup') # list all h files for strndup
        print conf.clib_info('strndup') # package.json as python dict


