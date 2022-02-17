import unittest
from chocolatetruffle import (
    from_approximate_size,
    approximate_size,
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

    def test_to_json(self) :
        for s in self.json_formatter_list :
            self.assertEqual(to_json(s[0], indent=None), s[1])


if __name__ == '__main__' :
    unittest.main()
