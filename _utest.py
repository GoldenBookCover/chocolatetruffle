import unittest
from os import remove
from chocolatetruffle import (
    from_approximate_size,
    approximate_size,
    delete_from_file,
    to_json,
)


class ChocolatetruffleTest(unittest.TestCase) :
    # TODO: Add more cases
    size_bytes_list = (
        ('54M', 56623104),
        ('8.0kb', 8192),
        ('1.5GiB', 1610612736),
    )
    bytes_size_list = (
        (56623104, '54.00 MiB'),
        (8192, '8.00 KiB'),
        (1610612736, '1.50 GiB'),
    )
    json_formatter_list = (
        ({'name': 'Alice', 'age': 18, 'caps': {'brave', 'smart', 'golden', 'blue'}},
            '{"name": "Alice", "age": 18, "caps": ["blue", "brave", "golden", "smart"]}'),
        ({'server_name': 's13501', 'email': 's13501@cbs.org', 'websites': set(), 'databases': set(), 'rsync': set(), 'preach': False, 'etc': {'s13501_zabbix', 's13501_etc', 's13501_admin_tools'}, 'clean_tomlog': None, 'clamav': {'0'}}, 
            '{"server_name": "s13501", "email": "s13501@cbs.org", "websites": [], "databases": [], "rsync": [], "preach": false, "etc": ["s13501_admin_tools", "s13501_etc", "s13501_zabbix"], "clean_tomlog": null, "clamav": ["0"]}'),
        ({ 'age', 'help', '12.0' },
            '["12.0", "age", "help"]'),
    )
    
    def test_from_approximate_size(self) :
        for s in self.size_bytes_list :
            self.assertEqual(from_approximate_size(s[0]), s[1])
    
    def test_approximate_size(self) :
        for s in self.bytes_size_list :
            self.assertEqual(approximate_size(s[0]), s[1])
    
    def test_delete_from_file(self) :
        with open('test_delete_line.txt', 'w') as ft :
            ft.write('line 1\n'
                     'line 2\n'
                     'line 3\n'
                     'line 4\n'
                     'line 5\n')
        # Delete line normally
        delete_from_file('test_delete_line.txt', 2, check_line=True)
        with open('test_delete_line.txt', 'r') as ft :
            self.assertEqual(ft.read(), 'line 1\nline 3\nline 4\nline 5\n')
        # Delete nonexistent line without assertion
        delete_from_file('test_delete_line.txt', 12)
        with open('test_delete_line.txt', 'r') as ft :
            self.assertEqual(ft.read(), 'line 1\nline 3\nline 4\nline 5\n')
        # Delete nonexistent line with assertion
        self.assertRaises(AssertionError, delete_from_file, 'test_delete_line.txt', 5, check_line=True)
        remove('test_delete_line.txt')

    def test_to_json(self) :
        for s in self.json_formatter_list :
            self.assertEqual(to_json(s[0], indent=None), s[1])


if __name__ == '__main__' :
    unittest.main()

