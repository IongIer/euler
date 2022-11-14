# What is the largest prime factor of the number 600851475143 ?

def get_factors(n):
    answer = []
    for f in range(1, int((n ** 0.5) + 1)):
        if n % f == 0:
            answer.append(f)
            answer.append(n//f)
    return answer

def is_prime(n):
    return len(get_factors(n)) == 2

def largest_prime(factors):
    largest = 0
    for factor in factors:
        if is_prime(factor) and factor > largest:
            largest = factor

    return largest

all_factors = get_factors(600851475143)

print(largest_prime(all_factors))
