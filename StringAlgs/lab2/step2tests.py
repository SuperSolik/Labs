import unittest
from step2 import AhoCorasick, prepare_patterns

param_list = [('ACT', ['A$', '$'], [0]),
              ('CCCC', ['C$$C', '$'], [0]),
              ('CCCAAA', ['C**A', '*'], [0, 1, 2]),
              ('ASDASDASD', ['A!!A!D', '!'], [0, 3]),
              ('ASLDALSNDLSADN', ['S#D', '#'], [1, 6, 10])]


class Test(unittest.TestCase):
    def test(self):
        for text, pat, ans in param_list:
            with self.subTest():
                patterns, ind_patterns = prepare_patterns(pat[0], pat[1])
                finder = AhoCorasick()
                finder.create_states(patterns)
                self.assertEqual(finder.find_joker(text, ind_patterns), ans)


if __name__ == '__main__':
    unittest.main()
