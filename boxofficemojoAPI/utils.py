__author__ = 'rastko'

import decorator


@decorator.decorator
def na_or_empty(func, *args):
    """Decorator for handling conversion of the Movie.Data member"""
    self = args[0]
    key = args[1]
    try:
        if key in self.Data:
            if self.Data[key].upper() != "N/A":
                return func(*args)
            else:
                self.Data[key] = None
        else:
            self.Data[key] = None
    except:
        print "Error cleaning: ", key
        raise
