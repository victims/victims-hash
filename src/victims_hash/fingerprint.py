
from archive.archive import Archive
from archive.reader.jar import JarReader
from archive.reader.gem import GemReader
from archive.reader.egg import EggReader

def fingerprint(file, io=None): 

    if not io:
        io = open(file, "r")
    
    if file.endswith(".jar"):
        return Archive(JarReader(io)).fingerprint()

    elif file.endswith(".gem"):
        return Archive(GemReader(io)).fingerprint()
        
    elif file.endswith(".egg"):
        return Archive(EggReader(io)).fingerprint()

    else:
        raise NotImplemtedError("No support for %s files." % file)

    
