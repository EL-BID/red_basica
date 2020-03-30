import os
import sys
import re
import inspect
from PyQt5 import QtWidgets
 
class FilePatcher:
    def __init__(self, path):
        self._path = path
        self._line_number = 1
        self._previous_line = None
        self._line = None
        self._parent_classes = []
        self._qtwidgets_imported = False
 
    def error(self, msg):
        print("ERROR: {}:{} {}".format(self._path,self._line_number, msg))
 
    def info(self, msg , *args):
        msg = msg + " ".join(args)
        print("INFO: {}:{} {}".format(self._path,self._line_number, msg))
 
    def patch(self):
        out = ""
        with open(self._path) as f:
            previous_line = None
            for self._line in f.readlines():
                self.fix_object_inheritance()
                self.get_parent_class()
                if self._previous_line:
                    self.error_double_init()
                self.fix_qt_widgets()
                self.fix_init_with_self()
                self.fix_super_with_argument()
                self.fix_call_without_super()
                self.error_import_missing()
                self._line_number += 1
                self._previous_line = self._line
                out += self._line
 
        with open(self._path, 'w+') as f:
            f.write(out)
 
    def get_parent_class(self):
        """Extract parent class to self._parent_classes var"""
        if self._line.startswith("class "):
            l = re.match(r".*\((.*)\):", self._line)
            if l:
                self._parent_classes = []
                for cls in l.group(1).split(","):
                    self._parent_classes.append(cls.strip())
 
    def fix_object_inheritance(self):
        """In Python3 you no longer need to inherit from object"""
 
        if ":" in self._line:
            self._line = re.sub(r"\(object\)", "", self._line)
 
    def error_double_init(self):
        """
        Detect double call to init and raise an error
        """
 
        if ".__init__" in self._previous_line and ".__init__" in self._line:
            self.error("Double init is no longer allowed")
 
    def fix_super_with_argument(self):
        """
        Thanks to Python 3 now we can call super() instead of super()
        """
        if re.match(r".*super\([^)].*", self._line):
            self._line = re.sub(r"super\([^)]+\)", "super()", self._line)
            self.info("Fix ", self._line.strip())
 
    def fix_init_with_self(self):
        """
        In some part of the code we have super().__init__(

        Now we can use super().__init__
        """
        if ".__init__(self" in self._line:
            self._line = re.sub(r"([A-Z\.a-z0-9_-]+)\.__init__\(self,? ?", "super().__init__(", self._line)
 
    def fix_call_without_super():
        """
        We need to call parent with super instead of class name in order to avoid issues
        """
 
        for cls in self._parent_classes:
            m = re.match(r"(.*)({})\.([a-zA-Z]+)\((self, ? ?)(.*)".format(cls), self._line)
            if m:
                fixed = m.group(1) + "super()." + m.group(3) + "(" + m.group(5) + "\n"
                self._line = fixed
 
    def fix_qt_widgets(self):
        """
        Replace QtGui by QtWidgets when require
        """
 
        if self._line.startswith("from ") and "import" in self._line and "QtGui" in self._line and not "QtWidgets" in self._line:
            self._line = self._line.strip() + ", QtWidgets\n"
 
        if "QtGui." in self._line:
            for name, obj in inspect.getmembers(QtWidgets):
                self._line = self._line.replace("QtGui." + name, "QtWidgets." + name)
 
    def error_import_missing(self):
        """
        Check if we use QtWidgets without QtGui
        """
        if "QtWidgets" in self._line:
            if " import " in self._line:
                self._qtwidgets_imported = True
            else:
                if self._qtwidgets_imported is False:
                    self.error("QtWidgets import missing")
 
for root, dirs, files in os.walk('.'):
  for file in files:
    if file.endswith('.py'):
        FilePatcher(os.path.join(root, file)).patch()
 
