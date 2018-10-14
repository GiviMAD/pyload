# -*- coding: utf-8 -*-

from pyload.plugins.internal.xfsaccount import XFSAccount


class NosuploadCom(XFSAccount):
    __name__ = "NosuploadCom"
    __type__ = "account"
    __version__ = "0.07"
    __pyload_version__ = "0.5"
    __status__ = "testing"

    __description__ = """Nosupload.com account plugin"""
    __license__ = "GPLv3"
    __authors__ = [("Walter Purcaro", "vuolter@gmail.com")]

    PLUGIN_DOMAIN = "nosupload.com"