#/bin/bash

python -c 'import sys; from victims_hash.fingerprint import fingerprint; print(fingerprint(sys.argv[1]))' $1
