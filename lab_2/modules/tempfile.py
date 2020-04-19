import os 
import uuid

from modules.useful import open_file


class TempFile:

    def __init__(self):
        self._createfile()

    def _createfile(self):
        self.filename = str(uuid.uuid1()) + "-temp" 
        self.file = open_file(self.filename, "w", "Can't create temp-file!")

    def push(self, text):
        self.file.write(str(text))

    def reload(self):
        old_name = self.filename
        self.file.close() 
        self._createfile()
        return old_name

    def flush(self):
        self.file.close()
        os.remove(self.filename)
        self._createfile()

    def __del__(self):
        self.file.close()
        os.remove(self.filename)
