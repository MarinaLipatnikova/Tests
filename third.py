import collections
def vote(votes):
    c = collections.Counter(votes)
    max =  float('-inf')
    key = 0
    for kkey, val in (c.items()):
        if val > max:
            max = val
            key = kkey
    return key
