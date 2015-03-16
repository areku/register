#
#
#
#
#
#
#
#

__author__ = "Alexander Weigl <Alexander.Weigl@student.kit.edu>"

__date__ = "2015-03-16"

__version__ = "0.1"

__all__ = ['FunctionRegister']

def get_name(obj):
    try:
        return obj.__name__
    except:
        try:
            return obj.func_name
        except:
            return None

class FunctionRegister(object):
    def __init__(self):
        self._register = dict()
        self._meta = dict()

    def register(self, fn, name, meta = None):
        self._meta[name] = meta or {}
        self._register[name] = fn

    def __call__(self, fn_or_name = None, **kwargs):
        if fn_or_name and callable(fn_or_name):
            name = get_name(fn_or_name)
            self.register(fn_or_name, name)
            return fn_or_name

        else:
            def r(fn):
                name = fn_or_name or get_name(fn)
                self.register(fn, name)
                return fn
            return r

    def lookup(self, name, default = None):
        return self._register.get(name, default)

