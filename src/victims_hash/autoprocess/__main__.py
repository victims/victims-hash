import argparse
import multiprocessing
import os.path
import pyinotify

from victims_hash.autoprocess.processor import process
from victims_hash.autoprocess import store


class EventHandler(pyinotify.ProcessEvent):
    """
    How to handle events from the watch.
    """

    def my_init(self, pool, store, topdir, config):
        """
        Additional items on creation of instance.

        :Parameters:
           - `pool`: Multiprocessing pool.
           - `store`: Callable that will store results (filename data)
           - `topdir`: Top directory everything processing should be under
        """
        self.pool = pool
        self.store = store
        self.topdir = topdir
        self.config = config

    def process_IN_CREATE(self, event):
        """
        How to process a create event.

        :Parameters:
           - `event`: The create event.
        """
        if event.pathname.startswith(self.topdir):
            self.pool.apply_async(
                process, (event.pathname, self.store, self.config))


def main():
    """
    Main entry point.
    """
    parser = argparse.ArgumentParser(prog="victims_hash.autoprocess")
    parser.add_argument(
        '-w', '--workers', default=2, type=int)
    parser.add_argument(
        '-d', '--directory', default=os.path.realpath('.'), type=str)
    parser.add_argument('-s', '--store', required=True, type=str)
    parser.add_argument('-c', '--config', default=None, type=str)

    args = parser.parse_args()
    args.directory = os.path.realpath(args.directory)
    print "Starting with %i workers, watching %s" % (
        args.workers, args.directory)

    config = {}
    if args.config:
        with open(args.config, 'r') as c_obj:
            for line in c_obj.readlines():
                key, value = line.split('=')
                config[key.strip()] = value.strip()

    pool = multiprocessing.Pool(args.workers)
    try:
        wm = pyinotify.WatchManager()
        notifier = pyinotify.Notifier(
            wm, EventHandler(pool=pool, store=getattr(
                store, args.store), topdir=args.directory, config=config))
        wm.add_watch(args.directory, pyinotify.IN_CREATE)
        notifier.loop()
    except Exception, ex:
        print ex
        pool.close()


if __name__ == '__main__':
    main()
