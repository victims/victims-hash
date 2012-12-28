
import zipfile

from victims_hash.archive.reader import ArchiveReader


class EggReader(ArchiveReader):

    def readinfo(self, hints={}):
        """
        Extract meta information from the archive.

        :Parameters:
           - `hints`: specify things to look for if available.
        """
        self.io.seek(0)
        metadata = {}

        with zipfile.ZipFile(self.io) as archive:
            with archive.open('EGG-INFO/PKG-INFO') as pkg_info:
                for line in pkg_info.readlines():
                    key, value = line.split(': ', 1)
                    metadata[key] = value[:-1]
        return metadata

    def readfiles(self):
        """
        Read files within the archive and return their content
        """
        self.io.seek(0)
        with zipfile.ZipFile(self.io) as archive:
            for filename in archive.namelist():
                if filename.endswith(".py"):
                    yield(filename, archive.read(filename))
