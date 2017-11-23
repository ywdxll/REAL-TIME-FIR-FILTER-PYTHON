# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8



from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_FIR', [dirname(__file__)])
        except ImportError:
            import _FIR
            return _FIR
        if fp is not None:
            try:
                _mod = imp.load_module('_FIR', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _FIR = swig_import_helper()
    del swig_import_helper
else:
    import _FIR
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class FIR(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FIR, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FIR, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _FIR.new_FIR()
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def getTaps(self):
        return _FIR.FIR_getTaps(self)

    def getCoeff(self, i):
        return _FIR.FIR_getCoeff(self, i)

    def getType(self):
        return _FIR.FIR_getType(self)

    def getFreq(self, i):
        return _FIR.FIR_getFreq(self, i)

    def getBuffer(self, i):
        return _FIR.FIR_getBuffer(self, i)

    def setTaps(self, M):
        return _FIR.FIR_setTaps(self, M)

    def setCoeff(self, x, i):
        return _FIR.FIR_setCoeff(self, x, i)

    def setType(self, a):
        return _FIR.FIR_setType(self, a)

    def setFreq(self, x, i):
        return _FIR.FIR_setFreq(self, x, i)

    def setBuffer(self, x, i):
        return _FIR.FIR_setBuffer(self, x, i)

    def lowpass(self, M, f):
        return _FIR.FIR_lowpass(self, M, f)

    def highpass(self, M, f):
        return _FIR.FIR_highpass(self, M, f)

    def stopband(self, M, f1, f2):
        return _FIR.FIR_stopband(self, M, f1, f2)

    def passband(self, M, f1, f2):
        return _FIR.FIR_passband(self, M, f1, f2)

    def filter(self, x):
        return _FIR.FIR_filter(self, x)
    __swig_destroy__ = _FIR.delete_FIR
    __del__ = lambda self: None
FIR_swigregister = _FIR.FIR_swigregister
FIR_swigregister(FIR)

# This file is compatible with both classic and new-style classes.


