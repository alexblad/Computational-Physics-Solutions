def isprime(n):
    #kmax=n**(1/2)
    for k in primes: 
        #if k>kmax:
        if n%k == 0:
            return False
    return True
    
primes= []
for n in range (2,10000):
    if isprime(n):
        primes.append(n)

print(primes)
print(len(primes))