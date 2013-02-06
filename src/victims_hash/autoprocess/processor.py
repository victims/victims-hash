
from victims_hash import fingerprint, metadata


def process(filename, store, config={}):
    data = {}
    data.update(fingerprint.fingerprint(filename))
    data.update(metadata.extract_metadata(filename))
    store(filename, data, config)
