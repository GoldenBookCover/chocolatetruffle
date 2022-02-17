"""
Providing some useful tools and functions.
Python 3.8 or above required.

If you want to use custom modules, do this first:
Install with pip
$ pip install https://github.com/MonstreCharmant/chocolatetruffle/archive/build_pkg.zip
Or add source code to custom path
$ git clone https://github.com/MonstreCharmant/chocolatetruffle.git
$ export PYTHONPATH="/path/to/parent_to_chocolatetruffle:$PYTHONPATH"
"""

__author__ = 'Monstre Charmant'
__version__ = '1.3.1'
__copyright__ = 'Copyright 2019-2022 Monstre Charmant'
__license__ = 'MIT'
__maintainer__ = __author__
__status__ = 'developing'
__email__ = 'ballonrage@gmail.com'
# __credits__ = ['{credit_list}']

__all__ = [
    'safely_get_element',
    'approximate_size',
    'from_approximate_size',
    'insert_into_file',
    'get_or_update_config',
    'delete_from_file',
    'jprint',
    'to_json',
    'password_generator',
]

from .systools import (
    safely_get_element,
    approximate_size,
    from_approximate_size,
    insert_into_file,
    get_or_update_config,
    delete_from_file
)

from .formatter import (
    jprint,
    to_json,
)

from .secretart import (
    password_generator,
)
