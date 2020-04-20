import os 
import uuid

from modules.useful import open_file


class TempFile:
    ERROR_WRITE = "Can't create file to write!"

    def __init__(self):
        self.filename = ""
        self.size = 0

    def _openfile(self):
        self.filename = str(uuid.uuid1()) + "-temp" 
        self.file = open_file(self.filename, "w", self.ERROR_WRITE)

    def _removefile(self, filename):
        try:
            os.remove(filename)
        except:
            pass

    def remove_files(self, filenames):
        [ self._removefile(i) for i in filenames ]

    def _closefile(self):
        self.filename = ""
        self.size = 0
        try:
            self.file.close()
        except:
            pass

    def push(self, text=""):
        if not self.filename:
            self._openfile()
        text = str(text)
        self.size += len(text)
        self.file.write(text)

    def free(self):
        filename = self.filename
        self._closefile()
        return filename

    def kill(self):
        filename = self.filename
        self._closefile()
        self._removefile(filename)

    def sizeof(self):
        return self.size

    def create_empty(self):
        filename = str(uuid.uuid1()) + "-temp" 
        with open_file(filename, "w", self.ERROR_WRITE) as file:
            pass
        return filename
