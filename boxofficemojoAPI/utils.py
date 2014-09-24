__author__ = 'rastko'

import decorator
import requests.exceptions
import time


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

@decorator.decorator
def catch_connection_error(func, *args):
    has_error = True
    while has_error is True:
        try:
            has_error = False
            return func(*args)
        except requests.exceptions.ConnectionError as e:
            has_error = True
            print e.message
            print "Too many HTTP requests. wait 10 sec."
            time.sleep(10)
        except:
            raise
