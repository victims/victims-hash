victims-hash
=============

Hashing mechanism used by victims to produce a unique fingerprint for a
given archive. Currently supports .jar, .gem, .egg files.

from victims_hash.fingerprint import fingerprint
data = fingerprint('file.jar')

