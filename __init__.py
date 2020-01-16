"""
Providing some useful tools and functions.
Python 3.8 required.

If you want to use custom modules, do this first:
>>> __import__('sys').path.insert(0, r'D:\Documents\py_modules')
"""

__author__ = 'Monstre Charmant'
__version__ = '1.2.2'
__copyright__ = 'Copyright 2019-2020 Monstre Charmant'
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

from .systools import (
    safely_get_element,
    approximate_size,
    from_approximate_size,
    insert_into_file,
    get_or_update_config,
)
