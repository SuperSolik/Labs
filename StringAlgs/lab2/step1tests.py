import unittest
from step1 import AhoCorasick

param_list = [('ACT', ['A', 'T'], [(0, 0), (2, 1)]),
              ('CCCA', ['C'], [(0, 0), (1, 0), (2, 0)]),
              ('ASDSAD VMCVASDTESTCASE', ['ASD', 'TEST'], [(0, 0), (11, 0), (14, 1)]),
              ('TTTTT', ['T'], [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]),
              ('ABCSAD', ['SAD', 'TEST'], [(3, 0)])]


class Test(unittest.TestCase):
    def test(self):
        for text, pat, ans in param_list:
            with self.subTest():
                finder = AhoCorasick()
                finder.create_states(pat)
                self.assertEqual(finder.find_all(text), ans)


if __name__ == '__main__':
    unittest.main()
