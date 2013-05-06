victims-hash
=============

Hashing mechanism used by victims to produce a unique fingerprint for a
given archive. Currently supports .jar, .gem, .egg files.

    from victims_hash.fingerprint import fingerprint
    data = fingerprint('file.jar')

[![Build Status](https://api.travis-ci.org/victims/victims-hash.png)](https://travis-ci.org/victims/victims-hash)
