"""
Providing some useful tools and functions.

If you want to use custom modules, do this first:
>>> __import__('sys').path.insert(0, r'D:\Documents\py_modules')
"""

__author__ = 'Monstre Charmant'
__version__ = '1.0.2'
__copyright__ = 'Copyright 2019, Chocolate Truffle'
__license__ = 'MIT'
__maintainer__ = __author__
__status__ = 'developing'
# __email__ = 'b***e@gmail.com'
# __credits__ = ['{credit_list}']

__all__ = [
    'safely_get_element',
    'approximate_size',
    'insert_into_file',
]

HUMANSIZE_SUFFIXES = {1000 : ('KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'),
                      1024 : ('KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB')}


def safely_get_element(from_list, i) :
    """Get an element from a list, a tuple and so on safely.

    Be cafeful when using this, because you will never receive
    an IndexError when accessing the elements, this may be
    what you want, or not.
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


def approximate_size(size, is_1024=True, unit=None) :
    """Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
    if False, use multiples of 1000
    unit -- in which unit you'd like to show the size
    Returns: string
    """
    if size < 0 :
        raise ValueError('number must be non-negative')

    multiple = 1024 if is_1024 else 1000
    if (unit is not None) and (unit not in HUMANSIZE_SUFFIXES[multiple]) :
        raise ValueError('invalid unit')

    for suffix in HUMANSIZE_SUFFIXES[multiple] :
        size /= multiple

        if unit is None and size < multiple :
            return '{0:.3f} {1}'.format(size, suffix)
        elif suffix == unit :
            return '{0:.3f} {1}'.format(size, suffix)

    raise ValueError('number too large')


def insert_into_file(file: str, num: int, line: str, check_line=False) -> None :
    """Insert a line into a file

    If the line number is greater than the total number of lines
    in the given file, the line will be appended to the end
    of the file, this may be what you what, or not.
    If you don't what this, set check_line=True to check the line
    number before insertion.
    :param file: the file to insert a line into
    :param num: the line number where the line is inserted
    :param line: the string to insert
    :param check_line: is a greater line number than the total number of lines allowed
    :return: None
    """

    with open(file, 'r') as fr :
        file_lines = fr.readlines()

    assert num > 0, 'invalid line number'
    if check_line :
        assert num <= len(file_lines) + 1, 'invalid line number'

    if num == len(file_lines) + 1 :
        line_ = "\n" + line + "\n"
    else :
        line_ = line + "\n"
    file_lines.insert(num - 1, line_)

    with open(file, 'w') as fw :
        for i in file_lines :
            fw.write(i)
