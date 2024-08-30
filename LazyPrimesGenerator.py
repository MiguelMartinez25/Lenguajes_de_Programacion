def lazy_primes_generator(n):
    if n<2:
        return False
    for i in range(2, int(n/2)+1):
        if n % i==0:
            return False
        return True

def numeros_primos():
    n = 2
    while True:
        if lazy_primes_generator(n):
            yield n
        n +=1

if __name__ == "__main__":
    primes = numeros_primos()

    primos = [next(primes)for _ in range(100)]
print(primos)






    