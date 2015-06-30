# iniital testing of canopy on Mac OS X for edX course MIT 6.00.1x
# Author: Joe Ryan
# takes two parameters and output some text lines

import sys

if len(sys.argv) < 2:
    print "You should pass in a name and an integer as"
    print "two command line arguments and see what happens."
else:
    for i in range(0, int(sys.argv[2])):
        print "Hello, %s!" % sys.argv[1]