
import zipfile
import javaclass

from victims_hash.archive.reader import ArchiveReader

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class JarReader(object):

    # TODO: Allow you to specify the things that extract / mine for
    # information within the JAR file.
    def readinfo(self, hints={}):
        """
        Extract meta information from the archive/

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
                if filename.endswith(".class"):
                    iostr = StringIO(archive.read(filename))
                    # Skip java compiler version.
                    javaclass.read_magic(iostr)
                    javaclass.read_version(iostr)
                    yield(filename, iostr.read())
