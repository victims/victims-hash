
import zipfile

class EggReader(object):

    def __init__(self, io):
        self.io = io

    # TODO
    def readinfo(self):
        """
        Extract meta information from the archive/
        """

        self.io.seek(0)
        metadata = {}

        with zipfile.ZipFile(self.io) as archive:
            for filename in archive.namelist():
                pass 


    def readfiles(self):
        """
        Read files within the archive and return their content 
        """

        self.io.seek(0)
        with zipfile.ZipFile(self.io) as archive: 
            for filename in archive.namelist():
                if filename.endswith(".py"):
                    yield(filename, archive.read(filename))
                    
