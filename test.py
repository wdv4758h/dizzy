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

    def test_jaro_winkler_distance(self):
        cases = [('martha', 'marhta', 0.961111111111111111),
                 ('jones', 'johnson', 0.8323809523809523),
                 ('dwayne', 'duane', 0.84),
                 ('dixon', 'dicksonx', 0.8133333333333332),
                 ('fvie', 'ten', 0),
                 ('al', 'al', 1.0),
                 ('henka', 'henkan', 0.9666666666666667),
                 ('abcvwxyz', 'cabvwxyz', 0.9583333333333333),
            ]

        for s1, s2, value in cases:
            self.assertEqual(dizzy.jaro_winkler_distance(s1, s2), value)

    def test_soundex(self):
        cases = [('Soundex', 'S532'),
                 ('Example', 'E251'),
                 ('Ciondecks', 'C532'),
                 ('Sownteks', 'S532'),
                 ('Ekzampul', 'E251'),
                 ('Euler', 'E460'),
                 ('Gauss', 'G200'),
                 ('Hilbert', 'H416'),
                 ('Knuth', 'K530'),
                 ('Lloyd', 'L300'),
                 ('Lukasiewicz', 'L222'),
                 ('Ellery', 'E460'),
                 ('Ghosh', 'G200'),
                 ('Heilbronn', 'H416'),
                 ('Kant', 'K530'),
                 ('Ladd', 'L300'),
                 ('Lissajous', 'L222'),
                 ('Wheaton', 'W350'),
                 ('Burroughs', 'B620'),
                 ('Burrows', 'B620'),
                 ("O'Hara", 'O600'),
                 ('Washington', 'W252'),
                 ('Lee', 'L000'),
                 ('Gutierrez', 'G362'),
                 ('Pfister', 'P236'),
                 ('Jackson', 'J250'),
                 ('Tymczak', 'T522'),
                 ('VanDeusen', 'V532'),
                 ('Ashcraft', 'A261'),
                 ('Ashcroft', 'A261'),
                 ('Robert', 'R163'),
                 ('Rupert', 'R163'),
                 ('Rubin', 'R150'),
            ]

        for s, value in cases:
            self.assertEqual(dizzy.soundex(s), value)

if __name__ == '__main__':
    unittest.main()
