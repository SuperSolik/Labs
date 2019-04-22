from source import *
import unittest


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(kmp('a', 'aaa'), [0, 1, 2])

    def test2(self):
        self.assertEqual(kmp('test', 'test'), [0])

    def test3(self):
        self.assertEqual(kmp('a', 'bb'), [-1])

    def test4(self):
        self.assertEqual(kmp('', 'aaaaa'), [1, 2, 3, 4, 5])

    def test5(self):
        self.assertEqual(kmp('asdsa', ''), [-1])


if __name__ == '__main__':
    unittest.main()
