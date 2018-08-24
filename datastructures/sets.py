'''
sets.py
Sets Practice

This is a code to practice sets in Python. That includes some of the
'''

# function that returns the element that is a member of a set OR a member of another set but not
# a member of both
def one_set_not_both(set_a, set_b):
    """
    Returns a set which contains any element that is
    a member of set_a OR a member of set_b but NOT a member
    of both.
    """
    a_and_b = set_a.intersection(set_b)
    a_or_b = set_a.union(set_b)
    return a_or_b - a_and_b


assert one_set_not_both(odds, primes) == set([9,1,2])
