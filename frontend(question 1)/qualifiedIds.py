import random 
def is_prime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2 == 0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True
def get_primes(n):
    primes=[]
    candidate=2
    while len(primes)<n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate+=1
    return primes
def get_fibonacci(n):
    fib=[0,1]
    while len(fib)<n:
        fib.append(fib[-1]+fib[-2])
    return fib[:n]
def get_even_numbers(n):
    return [i for i in range(2,2*n+1,2)]
def get_random_numbers(n,lower_bound=1,upper_bound=100):
    return [random.randint(lower_bound,upper_bound=100)for _ in range(n)]
def average_calculation(numbers):
    return sum(numbers)/len(numbers) if numbers else 0
