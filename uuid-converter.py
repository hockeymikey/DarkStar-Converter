#!/usr/bin/python

import os
import sys
import uuid as uid
import urllib2
import json
import re

force     = False
simulate  = False
dirname   = "."
timestamp = None
dashes    = True
upcase    = False
verbose   = False

reading_time = False
for arg in sys.argv[1:]:
    if reading_time:
        timestamp    = arg
        reading_time = False
    elif arg == "-s":
        simulate = True
    elif arg == "-D":
        dashes = False
    elif arg == "-f":
        force = True
    elif arg == "-u":
        upcase = True
    elif arg == "-v":
        verbose = True
    else:
        dirname = arg
        break

name_regex = re.compile("^[a-z0-9_]{1,16}$")
os.chdir(dirname)
for f in os.listdir("."):
    #print(os.path.splitext(f))[1]
    if "-" in f and (((os.path.splitext(f))[1] == ".json") or ((os.path.splitext(f))[1] == ".yml")):
        #print("herere")
        filename = f.split(os.extsep)[0]
        #print(filename)
        fileext  = os.extsep.join(f.split(os.extsep)[1:])
        #match    = name_regex.match(filename.lower())
        uuid = filename.translate(None, ''.join('-'))
        stat = os.stat(f)
        url  = "http://us.mc-api.net/v3/name/{0}" .format(uuid)
        if verbose:
            print(url)
        http = urllib2.urlopen(url)
        if http.code == 200:
            info = json.loads(http.read())
            name = info["name"]
            newfile = os.extsep.join([name, fileext])
            print("%s -> %s" % (f, newfile))
            if os.access(newfile, os.R_OK):
                print("File exists: %s" % newfile)
                if force:
                    print("(Force overwriting)")
                else:
                    print("(Skipping)")
                    continue
            if not simulate:
                os.rename(f, newfile)
        elif http.code == 204:
            print("Skipping %s - no Name known" % uuid)
        else:
            print("Website error")
            print("HTTP Code: %s" % http.code)
            print(http.read())
            break
print("All done!")
