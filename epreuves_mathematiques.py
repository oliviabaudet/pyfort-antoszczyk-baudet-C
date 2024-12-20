###factorielle###
import random
def factorielle(n):
    if n == 0:
        return 1
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

n = random.randint(1,10)
print(n)
print(factorielle(n))


