def is_prime(n):
    if n <= 3:
        return 'is prime'
    if not n%2 or not n%3:
        return 'is not prime'
    i = 5
    stop = int(n**0.5)
    while i <= stop:
        if not n%i or not n%(i + 2):
            return 'is not prime'
        i += 6
    return 'is prime'
