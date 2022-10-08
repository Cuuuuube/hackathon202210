"""
Command: prime_numbers
Return a list of all the prime numbers inferior or equal to n
"""
def prime_numbers(n):

    if n < 2:
        return False

    result = []
    for i in range(n+1):
        for i in range(2,n):
            if (n%i) == 0:
                break
        result.append(i)
    return result


"""
Command: sum_prime_numbers
Return a sum of all the prime numbers inferior or equal to n
"""
def sum_prime_numbers(n):
    return sum(prime_numbers(n))
