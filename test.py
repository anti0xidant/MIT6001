def primeTest(n):
    import math
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    else:
        return True

def primeGen():
    prime_bucket = []
    num = 1
    while True:
        num += 1
        for p in prime_bucket:
            if num % p == 0:
                break
        else:
            prime_bucket.append(num)
            yield num

