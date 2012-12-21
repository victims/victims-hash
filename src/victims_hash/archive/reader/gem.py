
import tarfile

class GemReader(object):

    def __init__(self, io):
        self.io = io

    #TODO
    def readinfo(self):
        """
        Extract meta information from the archive/
        """

        self.io.seek(0)
        metadata = {}

        with tarfile.open(self.io) as archive:
            for filename in archive.getnames():
                pass 


    def readfiles(self):
        """
        Read files within the archive and return their content 
        """

        self.io.seek(0)

        with tarfile.open(self.io) as archive: 
            for filename in archive.getnames():
                if filename.endswith(".rb"):
                    yield(filename, archive.extractfile(filename).read())
                    
