#!/usr/bin/python

import os
import sys
import uuid as uid
import urllib.request
import json
import re

force = False
simulate = False
dirname = "."

for arg in sys.argv[1:]:
    if arg == "-s":
        simulate = True
    elif arg == "-f":
        force = True
    else:
        dirname = arg
        break

name_regex = re.compile("^[a-z0-9_]{1,16}$")
os.chdir(dirname)

for f in os.listdir("."):

    if "-" in f and (((os.path.splitext(f))[1] == ".json") or ((os.path.splitext(f))[1] == ".yml")):

        filename = f.split(os.extsep)[0]
        fileext  = os.extsep.join(f.split(os.extsep)[1:])

        uuid = filename.replace('-', '')
        stat = os.stat(f)

        url = "https://mcapi.ca/profile/{0}" .format(uuid)
        http = urllib.request.urlopen(url)

        if http.code == 200:
            data = http.read().decode('utf8')
            info = json.loads(data)
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
            print("Skipping %s - no name known" % uuid)
        else:
            print("Website error")
            print("HTTP Code: %s" % http.code)
            print(http.read())
            break
print("Done and converted!")
