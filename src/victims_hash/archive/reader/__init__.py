"""
Archive reader classes.
"""


class ArchiveReader(object):
    """
    Master reader class.
    """

    def __init__(self, io):
        """
        Creates an instance of a reader.

        :Parameters:
           - `io`: File-like object.
        """
        self.io = io

    def readinfo(self, hints={}):
        """
        Extract meta information from the archive.

        :Parameters:
           - `hints`: specify things to look for if available.
        """
        raise NotImplementedError('readinfo must be implemented.')

    def readfiles(self):
        """
        Read files within the archive and return their content
        """
        raise NotImplementedError('readfiles must be implemented.')

    def __del__(self):
        """
        Always close the file on instance deletion.
        """
        if not self.io.closed:
            self.io.close()
