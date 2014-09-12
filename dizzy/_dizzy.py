def hamming_distance(s1, s2):
    '''return hamming distance

    s1, s2 are strings: return Hamming distance between two strings
    s1, s2 are intergers: return Hamming distance between two binary integers
    '''

    if isinstance(s1, str) and isinstance(s2, str):

        if len(s1) != len(s2):
            raise ValueError('Unequal length is unsupport')
        return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

    elif isinstance(s1, int) and isinstance(s2, int):

        return bin(s1^s2).count('1')

    else:
        raise ValueError('Unspport types')
