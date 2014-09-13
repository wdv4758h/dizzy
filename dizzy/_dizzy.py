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
