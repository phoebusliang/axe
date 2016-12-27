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
