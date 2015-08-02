#!/usr/bin/env python

import sys
# sys.argv has [script location, current room, text]

if __name__ == '__main__':
        try:
            print("/znc clearbuffer {}".format(sys.argv[1]))
        except:
            # silently fail because we dont want to print out to the room
            pass