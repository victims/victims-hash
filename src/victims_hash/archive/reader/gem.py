
import tarfile

from victims_hash.archive.reader import ArchiveReader


class GemReader(ArchiveReader):

    #TODO
    def readinfo(self, hints={}):
        """
        Extract meta information from the archive.

        :Parameters:
           - `hints`: specify things to look for if available.
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
