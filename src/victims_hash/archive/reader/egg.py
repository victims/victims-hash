
import zipfile

from victims_hash.archive.reader import ArchiveReader


class EggReader(ArchiveReader):

    # TODO
    def readinfo(self, hints={}):
        """
        Extract meta information from the archive.

        :Parameters:
           - `hints`: specify things to look for if available.
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
