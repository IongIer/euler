a,b = 1,2
total = 2
while b < 4000000:
    a,b = b, b + a
    if b < 4000000 and not b % 2:
        total += b
print(total)