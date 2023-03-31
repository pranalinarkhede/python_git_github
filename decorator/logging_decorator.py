# Logger decorator

def logger(fn):
    from datetime import datetime, timezone
    import time
    
    def inner(*args, **kwargs):
        called_at = datetime.now(timezone.utc)
        t1 = time.perf_counter()

        fn(*args, **kwargs)
        t2 = time.perf_counter()

        print('{0} executed. \nLogged at {1} executed in {2}s \n'.format(fn.__name__, called_at,round((t2-t1),4)))              
    return inner

@logger
def prime_func(a, b):
    primes = []
    for num in range(a, b + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)

@logger
def long_time_fn(n):
    for i in range(n):
        for j in range(100000):
            i*j
  

@logger
def factorial(n):
    fact = 1      
    for i in range(2, n+1):
        fact *= i
    return fact

@logger
def febonacci(n):
    a=1
    b=1
    if n==1:
        pass
    elif n==2:
        pass
    else:
        for i in range(n-3):
            total = a + b
            b=a
            a= total
        return b    
    

prime_func(2,50000)
febonacci(66785)
long_time_fn(3)
factorial(4678)
prime_func(2,750)
febonacci(200)