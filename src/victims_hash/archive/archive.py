import hashlib

class Archive(object):

    def __init__(self, reader, algorithms=["sha512", "sha1"]):
        self.reader = reader
        self.algorithms = algorithms

    def metadata(self):
        """
        Read all metadata associated with this archive
        """
        return {
            "meta" : self.reader.readinfo()
        }

    def filehash(self):
        try:
            self.reader.io.seek(0)
            digest = hashlib.sha512()
            for buff in iter(self.reader.io.read, b''):
                digest.update(buff)
            return digest.hexdigest()
        except:
            return ""
        finally:
            self.reader.io.seek(0)

    def fingerprint(self):
        """
        Create a fingerprint for this archive
        """
        hashes = {}

        for algorithm in self.algorithms:

            files = {}
            combined = hashlib.new(algorithm)

            for (filename, content) in self.reader.readfiles():
                h = hashlib.new(algorithm)
                h.update(content)

                checksum = h.hexdigest()
                files[checksum] = filename
                combined.update(checksum)

            hashes[algorithm] = {
                    "combined"  : combined.hexdigest(),
                    "files"     : files
            }

        return {
            "hash": self.filehash(),
            "hashes": hashes
        }
