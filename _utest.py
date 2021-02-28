import unittest
from os import remove
from chocolatetruffle import (
    from_approximate_size,
    approximate_size,
    delete_from_file
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


if __name__ == '__main__' :
    unittest.main()

