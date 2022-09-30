import checkIfPrime
from welcomeMessage import welcome_message

welcome_message()
check_if_prime = int(input('\nWhat number would you like to check to see if it is a prime number?\n'))

print(f'After checking, {check_if_prime}, {checkIfPrime.is_prime(check_if_prime)}.')