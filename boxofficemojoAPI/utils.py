__author__ = 'rastko'

import decorator
import requests.exceptions
import time
import re
import inflection
import bs4
from datetime import  datetime


@decorator.decorator
def na_or_empty(func, *args):
    """Decorator for handling conversion of the Movie.Data member"""
    data = args[0]
    key = args[1]
    try:
        if key in data:
            if data[key].upper() != "N/A" and data[key] != "-":
                return func(*args)
            else:
                data[key] = None
        else:
            data[key] = None
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


@na_or_empty
def convert_financial_field(data, key):
    """Formats financial values in the Data dictionary"""
    data[key] = re.sub(r'[(\xc2|\xa0|+|=|:|$|,)]', '', data[key])
    if key == "Production Budget":
        digits = re.findall(r'([\d\.\d]+)', data[key])
        digits = float(digits[0])
        if 'million' in data[key]:
            data[key] = digits*1000000.0
        elif 'thousand' in data[key]:
            data[key] = digits*1000.0
        else:
            data[key] = digits
    else:
        data[key] = float(data[key])


@na_or_empty
def convert_date_field(data, key):
    """Formats date values in the Data dictionary"""
    try:
        if len(re.findall(r'^(\w{3}) ', data[key])) == 0:
            data[key] = datetime.fromtimestamp(time.mktime(time.strptime(data[key], "%B %d, %Y")))
        else:
            data[key] = datetime.fromtimestamp(time.mktime(time.strptime(data[key], "%b %d, %Y")))
    except ValueError:
        data[key] = None
        pass


@na_or_empty
def convert_runtime_field(data, key):
    """Formats runtime values in the Data dictionary"""
    m = re.match(r"^((\d*) hrs\. )?(\d*)", data[key])
    if m.group(2) is None:
        data[key] = int(m.group(3))
    else:
        data[key] = int(m.group(2))*60 + int(m.group(3))


@na_or_empty
def convert_int_field(data, key):
    """Formats integer values in the Data dictionary"""
    data[key] = re.sub(r'[=|:|$|,)]', '', data[key])
    data[key] = int(data[key])

@na_or_empty
def convert_percent_field(data, key):
    """Formats integer values in the Data dictionary"""
    data[key] = re.sub(r'[(%|,)]', '', data[key])
    data[key] = float(data[key])*0.01


def standardize_keys(obj):
    if isinstance(obj, list):
        for element in obj:
            standardize_keys(element)
    elif isinstance(obj, dict):
        temp = []
        for key, val in obj.iteritems():
            standardize_keys(val)
            temp.append(key)
        for key in temp:
            obj[inflection.underscore(key.replace(" ", ""))] = obj.pop(key)
    else:
        pass


def get_soup(url):
    r = requests.get(url)
    if r.status_code == 200:
        return bs4.BeautifulSoup(r.content)
    else:
        return None