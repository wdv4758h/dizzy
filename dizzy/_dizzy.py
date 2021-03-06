from itertools import groupby

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

def levenshtein_distance(s1, s2):

    if isinstance(s1, str) and isinstance(s2, str):

        if s1 == s2: return 0

        len1, len2 = len(s1), len(s2)

        if not len1: return len2
        if not len2: return len1

        if len1 < len2:
            len1, len2 = len2, len1
            s1, s2 = s2, s1

        cur = list(range(len2+1))

        for i in range(1, len1+1):
            cur[0] = i
            last = i-1

            for j in range(1, len2+1):
                old = cur[j]
                cur[j] = min(cur[j]+1, cur[j-1]+1, last+(s1[i-1] != s2[j-1]))
                last = old

        return cur[len2]

    else:
        raise ValueError('Unspport types')

def damerau_levenshtein_distance(s1, s2):

    if isinstance(s1, str) and isinstance(s2, str):

        if s1 == s2: return 0

        len1, len2 = len(s1), len(s2)

        if not len1: return len2
        if not len2: return len1

        if len1 < len2:
            len1, len2 = len2, len1
            s1, s2 = s2, s1

        cur = list(range(len2+1))
        prev = cur.copy()

        for i in range(1, len1+1):
            pprev, prev = prev, cur.copy()
            cur[0] = i
            last = i-1

            for j in range(1, len2+1):
                old = cur[j]
                cur[j] = min(cur[j]+1, cur[j-1]+1, last+(s1[i-1]!=s2[j-1]))
                last = old

                if (i > 1 and j > 1
                        and s1[i-1] == s2[j-2] and s1[i-2] == s2[j-1]
                        and s1[i-1] != s2[j-1]):
                    cur[j] = min(cur[j], pprev[j-2]+1)

        return cur[len2]

    else:
        raise ValueError('Unspport types')

def jaccard_distance(s1, s2):
    '''jaccard distance
    http://en.wikipedia.org/wiki/Jaccard_index

    jaccard distance doesn't consider term frequency

    0 means equal, and 1 totally different
    '''

    set1, set2 = set(s1), set(s2)
    return 1 - len(set1 & set2) / len(set1 | set2)

def sorensen_distance(s1, s2):
    '''Sørensen distance
    http://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient

    0 means equal, and 1 totally different
    '''

    set1, set2 = set(s1), set(s2)
    return 1 - 2 * len(set1 & set2) / (len(set1) + len(set2))

def jaro_winkler_distance(s1, s2):
    '''
    http://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance
    '''

    if isinstance(s1, str) and isinstance(s2, str):

        len1, len2 = len(s1), len(s2)

        if not len1:
            if not len2:
                return 1
            return 0

        if len1 < len2:
            len1, len2 = len2, len1
            s1, s2 = s2, s1

        # match window
        window = len1//2 - 1
        match = 0
        matches = []
        for i in range(len2):
            if i-window > 0:
                j = i-window
            else:
                j = 0
            if s2[i] in s1[j:i+window+1]:
                match += 1
                matches.append(j + s1[j:i+window+1].index(s2[i]))

        if not match:
            return 0

        # trans transpositions need in matches
        trans = 0
        for i, j in zip(matches, sorted(matches)):
            trans += i != j

        # get max common prefix
        prefix = 0
        for i, j in zip(s1, s2):
            if i == j:
                prefix += 1
            else:
                break

        # prefix max is 4 ...
        if prefix > 4:
            prefix = 4

        # transpositions need to be floor
        d = (   match / len1
              + match / len2
              + (match - trans//2) / match )
        d = 1/3 * d

        jw = d + prefix * 0.1 * (1 - d)

        return jw

    else:
        raise ValueError('Unspport types')

def soundex(s):
    '''
    http://en.wikipedia.org/wiki/Soundex
    http://rosettacode.org/wiki/Soundex#Python

    b, f, p, v -> 1
    c, g, j, k, q, s, x, z -> 2
    d, t -> 3
    l -> 4
    m, n -> 5
    r -> 6

    two letters with the same number separated by 'h' or 'w' are coded as a single number
    '''

    codes = ('bfpv','cgjkqsxz', 'dt', 'l', 'mn', 'r')
    sound = { key: str(index+1) for index, string in enumerate(codes) for key in string }

    cmap = lambda key: sound.get(key, '9')  # '9' if not found (default is None)
    s = s.replace('h', '').replace('w', '')
    sdx = ''.join(cmap(key) for key in s.lower())
    sdx2 = s[0].upper() + ''.join(k for k, g in tuple(groupby(sdx))[1:] if k!='9')
    sdx3 = sdx2[0:4].ljust(4, '0')

    return sdx3
