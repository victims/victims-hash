#!/usr/bin/python

import sys
from victims_hash.fingerprint import fingerprint

if __name__ == "__main__":
    filename = sys.argv[1]
    if filename is None:
        print('Usage: python fingerprint <file>')
    print(fingerprint(filename))


