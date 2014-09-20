#import csv
import unittest
import dizzy

class TestDizzy(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #reader = csv.reader(open('test.csv', 'r'))
        #self.header = next(reader)
        #self.data = tuple(reader)

    #def test_distance(self):
    #    distance = ['hamming', 'levenshtein', 'damerau_levenshtein', 'jaccard', 'sorensen']

    #    for d in distance:
    #        for case in self.data:
    #            s1, s2, value = case[:2], case[self.header.index(d)]
    #            self.assertEqual(eval('dizzy.{}_distance(s1, s2)'.format(d), value))

    def test_hamming_distance(self):
        cases = [('', '', 0),
                 ('kitten', 'sittin', 2),
            ]

        for s1, s2, value in cases:
            self.assertEqual(dizzy.hamming_distance(s1, s2), value)

    def test_levenshtein_distance(self):
        cases = [('', '', 0),
                 ('abc', '', 3),
                 ('bc', 'abc', 1),
                 ('kitten', 'sitting', 3),
                 ('Saturday', 'Sunday', 3),
            ]

        for s1, s2, value in cases:
            self.assertEqual(dizzy.levenshtein_distance(s1, s2), value)

    def test_damerau_levenshtein_distance(self):
        cases = [('', '', 0),
                 ('abc', '', 3),
                 ('bc', 'abc', 1),
                 ('abc', 'acb', 1),
            ]

        for s1, s2, value in cases:
            self.assertEqual(dizzy.damerau_levenshtein_distance(s1, s2), value)

    def test_jaccard_distance(self):
        cases = [('decide', 'resize', 0.7142857142857143)]

        for s1, s2, value in cases:
            self.assertEqual(dizzy.jaccard_distance(s1, s2), value)

    def test_sorensen_distance(self):
        cases = [('decide', 'resize', 0.5555555555555556)]

        for s1, s2, value in cases:
            self.assertEqual(dizzy.sorensen_distance(s1, s2), value)

if __name__ == '__main__':
    unittest.main()
