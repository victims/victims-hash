
import zipfile
import javaclass

from victims_hash.archive.reader import ArchiveReader

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


def read_manifest(manifest):
    """
    Extract the information from the MANIFEST.MF file included with 
    the JAR file. 

    Parameters: 
        - `manifest`: File like object to extract the metadata from.
    """

    metadata = {}
    for line in manifest.readlines():

        if ':' in line:

            kw, sep, val = line.partition(':') 
            if kw.endswith('http') and val.startswith('//'):
                metadata[keyword] += line.rstrip()

            else:
                keyword = kw
                metadata[keyword] = val.rstrip()

        else:
            metadata[keyword] += line.rstrip()
 
    return metadata


def read_pom_properties(properties):
    """
    Extract meta information from the pom.properties file. This usually
    includes the artifact id, group id, and version information as per 
    the maven central repository. 

    Parameters: 
        - `properties`: File like object to extract the metadata from
    """

    metadata = {}

    for line in properties: 
        
        if line.startswith('#'):
            continue

        key, sep, value = line.partition('=')
        metadata[key] = value.rstrip()

    return metadata

class JarReader(ArchiveReader):

    def readinfo(self, hints={}):
        """
        Extract meta information from the archive/

        :Parameters:
           - `hints`: specify things to look for if available.
        """
        self.io.seek(0)
        metadata = []

        with zipfile.ZipFile(self.io) as archive:
    
            manifest_file = "META-INF/MANIFEST.MF"
            with archive.open(manifest_file) as manifest:
                metadata.append({
                    "filename"  : manifest_file,
                    "properties": read_manifest(manifest)})

            pom_properties = filter(lambda x: x.endswith('pom.properties'),\
                archive.namelist())

            if len(pom_properties) > 0:
                pom = pom_properties.pop(0)
                with archive.open(pom) as properties: 
                    metadata.append({
                        "filename" : pom, 
                        "properties" : read_pom_properties(properties)})

        return metadata

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
