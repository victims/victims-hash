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
        
    def fingerprint(self):
        """
        Create a fingerprint for this archive
        """

        hashes = {}
        
        for algorithm in self.algorithms: 
            
            files = {}
            combined = hashlib.new(algorithm)

            for (file, content) in self.reader.readfiles():
                h = hashlib.new(algorithm)
                h.update(content)

                # mongo doesn't like '.' in keyname
                key = file.replace('.', '[dot]')
                files[key] = h.hexdigest()
                combined.update(files[key])

            hashes[algorithm] = { 
                "combined"  : combined.hexdigest(), 
                "files"     : files
            }

        return {
            "hashes": hashes
        }
