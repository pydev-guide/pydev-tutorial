"""Lovely Spam! Wonderful Spam!"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pydev-tutorial")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Erik Torgrimson"
__email__ = "erik.torgrimson@example.com"
