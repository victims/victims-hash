import zipfile

# e.g. 
#for (filename, content) in get_content("commons-lang-2.6.jar"):
#
def get_content(jarfile):
    with zipfile.ZipFile(jarfile) as jar:
        for filename in jar.namelist():
            if not filename.endswith("/"): 
                yield (filename, jar.read(filename))

