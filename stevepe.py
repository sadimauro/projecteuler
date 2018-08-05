#!/usr/bin/python3

import math
import itertools

def isPrime(a):
    """
    >>> isPrime(1)
    False
    
    >>> isPrime(2)
    True

    >>> isPrime(3)
    True

    >>> isPrime(4)
    False

    >>> isPrime(25)
    False

    >>> isPrime(27)
    False

    >>> isPrime(29)
    True
    """
    if a <= 0:
        return False
   
    # 1 is not prime
    if a == 1:
        return False

    # 2 is prime
    if a == 2:
        return True
    
    # all other evens are not prime
    if a % 2 == 0:
        return False

    # check odd divisors between 3 and sqrt(a)
    #for i in range(3, math.floor(math.sqrt(a))+1, 2):
    for i in range(3, int(math.sqrt(a))+1, 2):
        if a % i == 0:
            return False

    return True

def isComposite(n):
    return not isPrime(n)

def getNextOddPrime(n):
    """
    Return next odd prime greater than n.
    n is expected to be odd.
    """
    n += 2
    while True:
        if isPrime(n):
            return n
        n += 2

def getPrimesBelow(n):
    """
    Return a list of the primes strictly below n.

    >>> getPrimesBelow(-3)
    []

    >>> getPrimesBelow(2)
    []

    >>> getPrimesBelow(3)
    [2]

    >>> getPrimesBelow(8)
    [2, 3, 5, 7]

    >>> getPrimesBelow(13)
    [2, 3, 5, 7, 11]

    """
    return getPrimesBetween(1, n)

def getPrimesBetween(m, n):
    """
    Return the list of primes strictly greater than
    m and strictly less than n.

    >>> getPrimesBetween(64, -3)
    []

    >>> getPrimesBetween(0, 2)
    []

    >>> getPrimesBetween(1, 3)
    [2]

    >>> getPrimesBetween(1, 8)
    [2, 3, 5, 7]

    >>> getPrimesBetween(1, 13)
    [2, 3, 5, 7, 11]

    >>> getPrimesBetween(2, 13)
    [3, 5, 7, 11]

    >>> getPrimesBetween(8, 13)
    [11]
    """

    ret = list()
    if m >= n:
        return ret
    if n <= 2:
        return ret

    if m <= 1:
        ret.append(2)
    
    if n <= 3:
        return ret
    
    if m % 2 == 0:
        m = m - 1
    i = getNextOddPrime(m)
    while i < n:
        ret.append(i)
        i = getNextOddPrime(i)
    return ret

def getPrimesBelowBySieve(n):
    """
    Return a list of the primes strictly below n.
    Calculate by using the Sieve of Eratosthenes.

    This is a *lot* faster than getPrimesBelow().
    >>> getPrimesBelowBySieve(-3)
    []

    >>> getPrimesBelowBySieve(2)
    []

    >>> getPrimesBelowBySieve(3)
    [2]

    >>> getPrimesBelowBySieve(8)
    [2, 3, 5, 7]

    >>> getPrimesBelowBySieve(13)
    [2, 3, 5, 7, 11]

    """
    ret = list()
    if n <= 2:
        return ret
    boolList = list()
    for i in range(n):
        boolList.append(True)
    boolList[0] = False; boolList[1] = False
    for i in range(2,math.floor(math.sqrt(n))+1):
        if boolList[i]:
            for j in range(i**2, n, i):
                boolList[j] = False
    for i in range(len(boolList)):
        if boolList[i]:
            ret.append(i)
    return ret

def getPrimesBetweenBySieve(m,n):
    """
    Return the list of primes strictly greater than
    m and strictly less than n.

    >>> getPrimesBetweenBySieve(64, -3)
    []

    >>> getPrimesBetweenBySieve(0, 2)
    []

    >>> getPrimesBetweenBySieve(1, 3)
    [2]

    >>> getPrimesBetweenBySieve(1, 8)
    [2, 3, 5, 7]

    >>> getPrimesBetweenBySieve(1, 13)
    [2, 3, 5, 7, 11]

    >>> getPrimesBetweenBySieve(2, 13)
    [3, 5, 7, 11]

    >>> getPrimesBetweenBySieve(8, 13)
    [11]
    """
    primes = getPrimesBelowBySieve(n)
    i = 0
    while i < len(primes):
        if primes[i] > m:
            break
        i += 1
    if i == len(primes):
        return []
    return primes[i:]

def getFactors(n):
    """
    Return a list containing the factors of n, 
    including 1 and n itself.
    """
    list2d = [[1], getPrimeFactors(n), [n]]
    return list(itertools.chain.from_iterable(list2d))

def getPrimeFactors(n):
    """
    Return a list containing the factors of n,
    not including 1 and n itself.

    >>> getPrimeFactors(-3)
    []

    >>> getPrimeFactors(0)
    []

    >>> getPrimeFactors(1)
    []

    >>> getPrimeFactors(2)
    []

    >>> getPrimeFactors(4)
    [2, 2]

    >>> getPrimeFactors(7)
    []

    >>> getPrimeFactors(18)
    [2, 3, 3]

    >>> getPrimeFactors(64)
    [2, 2, 2, 2, 2, 2]

    >>> getPrimeFactors(238202)
    [2, 119101]
    """
    ret = list()

    if n < 4:
        return ret

    primesToTry = getPrimesBelow(n)
    i = 0
    while i < len(primesToTry) and primesToTry[i] <= n:
        if n % primesToTry[i] == 0:
            ret.append(primesToTry[i])
            n = n // primesToTry[i]
        else:
            i += 1

    return ret

def isStrPandigital(n):
    nSet = set(n)
    return len(nSet) == len(n) and min(nSet) == '1' and max(nSet) == str(len(n))

def isIntPandigital(n):
    """Return True if n is pandigital, False otherwise.

    We shall say that an n-digit number is pandigital if it makes 
    use of all the digits 1 to n exactly once; for example, the 
    5-digit number, 15234, is 1 through 5 pandigital.

    >>> isIntPandigital(12345)
    True

    >>> isIntPandigital(15243)
    True

    >>> isIntPandigital(1)
    True

    >>> isIntPandigital(14326)
    False

    >>> isIntPandigital(14445)
    False
    """

    return isStrPandigital(str(n))

def tupleToInt(tupIn):
    res = 0
    for i in range(len(tupIn)):
        res *= 10
        res += int(tupIn[i])
    return res

def isPentagonal(n):
    """
    Return True is n is pentagonal, i.e. if 
      n = k(3k-1)/2 for some value k.

    >>> isPentagonal(0)
    False

    >>> isPentagonal(1)
    True

    >>> isPentagonal(5)
    True

    >>> isPentagonal(117)
    True

    >>> isPentagonal(118)
    False

    >>> isPentagonal(-3)
    False
    """
    if n <= 0:
        return False

    maybeNat = (math.sqrt((24*n)+1) + 1) / 6
    return maybeNat == int(maybeNat)

def isHexagonal(n):
    """
    Return True is n is pentagonal, i.e. if 
      n = k(3k-1)/2 for some value k.

    >>> isHexagonal(0)
    False

    >>> isHexagonal(1)
    True

    >>> isHexagonal(6)
    True

    >>> isHexagonal(231)
    True

    >>> isHexagonal(250)
    False

    >>> isHexagonal(-3)
    False
    """
    if n <= 0:
        return False

    maybeNat = (math.sqrt((8*n)+1) + 1) / 4
    return maybeNat == int(maybeNat)

def isTriangular(n):
    """
    Return True if n is triangular, i.e. if
      n = k(k+1)/2 for some integer k.

    >>> isTriangular(1)
    True

    >>> isTriangular(0)
    False

    >>> isTriangular(15)
    True

    >>> isTriangular(16)
    False

    >>> isTriangular(-3)
    False
    """
    if n <= 0:
        return False
    maybeSq = math.sqrt((8*n) + 1)
    return maybeSq == int(maybeSq)

def isSquare(n):
    """
    Return n if n is a square > 0, False otherwise.
    """
    if n < 0:
        return False
    temp = math.sqrt(n)
    return temp == int(temp)

def getNextSquare(n):
    """
    Return the next number greater than n that is a square.
    """
    n += 1
    while True:
        if isSquare(n):
            return n
        n += 1

def getIntPermutations(n):
    """
    Return a set filled with all of the permutations of
    int n, including n itself.

    e.g. if n = 123, return is {123, 132, 213, 231, 312, 321}.
    
    >>> getIntPermutations(1)
    {1}

    >>> getIntPermutations(12)
    {12, 21}

    >>> getIntPermutations(123)
    {321, 132, 231, 213, 312, 123}

    >>> getIntPermutations(144)
    {144, 441, 414}
    """
    ret = set()
    iter = itertools.permutations(str(n))
    for tup in iter:
        ret.add(tupleToInt(tup))
    return ret

if __name__ == "__main__":
    import doctest
    doctest.testmod()
