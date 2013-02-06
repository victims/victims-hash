
def echo(filename, data, config):
    """
    Prints results out for testing.
    """
    print filename, data


def mongo(filename, data, config):
    """
    Saves back to mongodb.

    Config expected to be like so::

       host=127.0.0.1
       port=1234
       database=mydb
       collection=data
    """
    from pymongo import Connection

    connection = Connection(config['host'], config['port'])
    db = getattr(connection, config['database'])
    db[config['collection']].insert(data)
