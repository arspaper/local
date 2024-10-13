import fnmatch



def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True



for i in range(0, 10**7):
    if isPrime(i):
        if fnmatch.fnmatch(str(i),'3?1111*'):
            print(i)