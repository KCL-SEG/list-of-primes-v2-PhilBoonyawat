"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes > 0:
        list = []
        num = 2
        list.append(num)
        num = num + 1
        while len(list) < number_of_primes:
            for divisor in range(2,num):
                if num % divisor == 0:
                    break
            else:
                list.append(num)
            num += 1

        return list
    else:
        raise ValueError(f"{number_of_primes} should be positive")
