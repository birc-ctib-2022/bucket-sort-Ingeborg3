"""Module for bucket sorting."""

from typing import Any

# Hvad menes med, at denne bucket sort har samme amortized complexity?

def count_keys(keys: list[int]) -> list[int]:
    """
    Count how many times we see each key in `keys`.

    You can assume that all elements in `keys` are
    non-negative. This is not a requirement for
    bucket sort in general--it can handle negative
    numbers--but it is a little more complicated and
    we will keep it simple here.

    You should return a list, `counts`. The list you
    return should have `len(counts) == max(keys) + 1`
    so we can index into any key (including those
    that might not be included in `keys`) and for each
    key `0 <= k <= max(keys)` `counts[k]` should be
    the number of times `k` occurs in `x`.

    The function should take time `O(len(keys))` and
    not more.

    >>> count_keys([1, 2, 2, 1, 4])
    [0, 2, 2, 0, 1]
    """
    # we can get the strict upper bound for the keys from keys if
    # keys is non-empty. Otherwise we must assume that
    # there are no keys.
    m = max(keys) + 1 if keys else 0
    counts = [0] * m # if m=0, counts=[]
    # The above corresponds to:
    #if keys:
    #    m = max(keys)+1
    #else: 
    #    m=0 
    for key in keys:
        counts[key] += 1
    return counts

print(count_keys([1,2,2,1,4]))

def count_sort(x: list[int]) -> list[int]:
    """
    Sort the values in x using count sort.

    The values in x must satisfy the constraints
    mentioned in `count_keys()`.

    >>> count_sort([])
    []
    >>> count_sort([1, 2, 1, 2, 4])
    [1, 1, 2, 2, 4]
    """
    # Count-sort where the output list have the final length to begin
    # with.
    counts = count_keys(x)
    out = [0]*len(x)
    j = 0
    for key in range(max(x)+1): # Iterate over all keys. 
        for i in range(j, counts[key]+j):
            out[i]=key
        j += counts[key]

    # Simple count-sort where output list is growing. 
    #counts = count_keys(x)
    #out = [] # otherwise out = [0] * len(x)
    #for key, count in enumerate(counts):
    #    out.extend([key]*count)
    return out

print('Count sort:')
print(count_sort([1, 2, 1, 2, 4]))


def cumsum(x: list[int]) -> list[int]:
    """
    Calculate the cumulative sum of x.

    >>> cumsum([1, 2, 3])
    [0, 1, 3] # Hvis cumulative sum, burde det ikke være [1, 3, 6]?
    >>> cumsum([0, 2, 2, 0, 1])
    [0, 0, 2, 4, 4] # Bør dette ikke være [0, 2, 4, 4, 5]? Så ville det
    # ikke virke, da første idx af output listen er 0. 
    """
    # x=counts=buckets.  
    out = x
    k = 0 # antager, at der ikke er 
    for i in range(1, len(x)):
        out[i], k = k + out[i-1], x[i]        
    return out

print('Cumsum:')
print(cumsum([0, 2, 2, 0, 1]))

def bucket_sort(x: list[tuple[int, Any]]) -> list[tuple[int, Any]]:
    """
    Sort the keys and values in x using count sort.

    The keys in x must satisfy the constraints
    mentioned in `count_keys()`.

    >>> bucket_sort([])
    []
    >>> bucket_sort([(1, "a"), (2, "b"), (1, "c"), (2, "d"), (4, "e")])
    [(1, 'a'), (1, 'c'), (2, 'b'), (2, 'd'), (4, 'e')]
    """
    buckets = cumsum(count_keys([k for k, _ in x]))
    out = [(0, None)] * len(x)
    # Place the pairs in their buckets
    for i in range(len(x)):
        out[buckets[x[i][0]]]= x[i]
        buckets[x[i][0]] += 1
    return out

print(bucket_sort([(1, "a"), (2, "b"), (1, "c"), (2, "d"), (4, "e")]))
