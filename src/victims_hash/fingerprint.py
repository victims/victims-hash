
from archive.archive import Archive
from archive.reader.jar import JarReader
from archive.reader.gem import GemReader
from archive.reader.egg import EggReader


def fingerprint(file, io=None):

    archive_instance = None
    if not io:
        io = open(file, "r")

    try:
        if file.endswith(".jar"):
            archive_instance = Archive(JarReader(io)).fingerprint()

        elif file.endswith(".gem"):
            archive_instance = Archive(GemReader(io)).fingerprint()

        elif file.endswith(".egg"):
            archive_instance = Archive(EggReader(io)).fingerprint()

        if not archive_instance:
            raise NotImplemtedError("No support for %s files." % file)
        return archive_instance

    except Exception, ex:
        # Blind raising ...
        raise ex
    finally:
        # Always make sure the file is closed.
        if not io.closed:
            io.close()
