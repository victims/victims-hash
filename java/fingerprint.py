import hashlib
import classdata
import jarfile
import StringIO as io

def hash_class(content): 
    
    f = io.StringIO(content)
    
    classdata.read_magic(f)
    classdata.read_version(f)
    h = hashlib.sha1()
    h.update(f.read())

    return h.hexdigest()


def create(jar):
    
    inventory = {}
    master = hashlib.sha1()
    for (file, content) in jarfile.get_content(jar):
        if file.endswith(".class"):
            h = hash_class(content)
            inventory[file] = h
            master.update(h)

    return { "combined" : master.hexdigest(), "files": inventory }
    

