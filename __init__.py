"""
Providing some useful tools and functions.
Python 3.8 required.

If you want to use custom modules, do this first:
>>> __import__('sys').path.insert(0, r'D:\Documents\py_modules')
"""

__author__ = 'Monstre Charmant'
__version__ = '1.2.0'
__copyright__ = 'Copyright 2019, Chocolate Truffle'
__license__ = 'MIT'
__maintainer__ = __author__
__status__ = 'developing'
# __email__ = 'b***e@gmail.com'
# __credits__ = ['{credit_list}']

__all__ = [
    'safely_get_element',
    'approximate_size',
    'from_approximate_size',
    'insert_into_file',
    'get_or_update_config',
]

import json


def safely_get_element(from_list, i) :
    """Get an element from a list, a tuple and so on safely.

    Be cafeful when using this, because you will never receive
    an IndexError when accessing the elements, this may be
    what you want, or NOT.
    >>> element_1 = safely_get_element(a_list, 2)
    :param from_list: the list to pick an element from
    :param i: the index of the element
    :return: an element or None
    """
    try :
        e = from_list[i]
    except IndexError :
        return None
    else :
        return e


def approximate_size(size: int, unit=None) :
    """Convert a size in bytes to human-readable form.

    :param size: size in bytes
    :param unit: in which unit you want to show the size
    return: string
    """

    HUMANSIZE_SUFFIXES = ('KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB')
    if (size := int(size)) < 0 :
        raise ValueError('number must be non-negative')

    if (unit is not None) and (unit not in HUMANSIZE_SUFFIXES) :
        raise ValueError("invalid unit, choose from {}".format(HUMANSIZE_SUFFIXES))

    for suffix in HUMANSIZE_SUFFIXES :
        size /= 1024

        if unit is None and size < 1024 :
            return "{0:.2f} {1}".format(size, suffix)
        elif suffix == unit :
            return "{0:.2f} {1}".format(size, suffix)

    raise ValueError('number too large')


def from_approximate_size(size: str) :
    """Convert a formatted size to bytes

    :param size: size to convert
    return: number of bytes
    """

    HUMANSIZE_SUFFIXES = (
        ('B', 'KIB', 'MIB', 'GIB', 'TIB', 'PIB', 'EIB', 'ZIB', 'YIB'),
        ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'),
        ('B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    )
    unit = ''

    # Split the number and unit
    while(size[-1].isalpha()) :
        unit = size[-1].upper() + unit
        size = size[:-1]
    
    size = float(size) if '.' in size else int(size)
    # Multiply the size by (index of unit)
    for h in HUMANSIZE_SUFFIXES :
        if unit in h :
            return size * (1024 ** h.index(unit))
    
    raise ValueError('unrecognized unit')


def insert_into_file(file: str, num: int, line: str, /, check_line=False, encoding_='utf-8') -> None :
    """Insert a line into a file

    If the line number is greater than the total number of lines
    in the given file, the line will be appended to the end
    of the file, this may be what you what, or not.
    If you don't what this, set check_line=True to check the line
    number before insertion.

    :param file: the file to insert a line into
    :param num: the line number where the line is inserted
    :param line: the string to insert
    :param check_line: allow a greater line number than the total number of lines
    :return: None
    """

    # TODO: use something more efficient
    with open(file, 'r', encoding=encoding_) as fr :
        file_lines = fr.readlines()

    assert (num := int(num)) > 0, 'invalid line number'
    if check_line :
        assert num <= len(file_lines) + 1, 'invalid line number'

    if num > len(file_lines) :
        line_ = "\n" + line + "\n"
    else :
        line_ = line + "\n"
    file_lines.insert(num - 1, line_)

    with open(file, 'w', encoding=encoding_) as fw :
        for i in file_lines :
            fw.write(i)


def get_or_update_config(config_file: str, option_name: str, /, value_=None, encoding_='utf-8') :
    """JSON & file based configuration management

    params: config_file: configuration file name
    params: option_name: option name
    params: value_: specify a new value if you want to update the option
    params: encoding_: file encoding, default to utf-8
    return: value: the value of the option
    return: updated: True if the value is updated and dumped into file
    """

    updated = False
    stored_value = {}
    
    # Read configurations from the configuration file
    with open(config_file, 'r', encoding=encoding_) as f :
        # If value exists, take it from the file
        stored_value.update(json.load(f))
        if stored_value.get(option_name) :
            value = stored_value[option_name]
        # If not, write the given value to the config file
        elif value_ is not None :
            value = value_  # ''.join(random.choices(characters_digits, k=length))
            stored_value.update({option_name: value})
            updated = True
        else :
            value = None
    
    # Dump into the configuration file if the value is updated
    if updated :
        try :
            with open(config_file, 'w', encoding=encoding_) as f :
                json.dump(stored_value, f, indent=4)
        except Exception :
            updated = False

    return value, updated
