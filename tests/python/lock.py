import fcntl


class Lock:
    def __init__(self, filename):
        self.filename = filename
        self.handle = open(filename, 'w')

    def acquire(self):
        fcntl.flock(self.handle, fcntl.LOCK_EX)

    def release(self):
        fcntl.flock(self.handle, fcntl.LOCK_UN)

    def __del__(self):
        self.handle.close()


lock_for_7p = Lock("/tmp/7p.lock")
lock_for_6sp = Lock("/tmp/6sp.lock")

locks = {"7p": lock_for_7p, "6sp": lock_for_6sp}
