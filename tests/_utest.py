import unittest
from __init__ import (
    from_approximate_size,
    approximate_size,
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


if __name__ == '__main__' :
    unittest.main()

