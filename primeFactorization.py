def primeFactorization(n) -> int: # Return the prime factorization of n.
    factors = []
    divisor = 2

    while n > 1:
        exponent = 0
        while n % divisor == 0:
            n //= divisor
            exponent += 1
        if exponent > 0:
            factors.append((divisor, exponent))
        divisor += 1
    
    return factors
            




print(primeFactorization(100))

