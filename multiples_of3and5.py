unique = set()
total = 0
for i in range(0,1000,3):
    unique.add(i)
    total += i
for i in range(0,1000,5):
    if i not in unique:
        total += i
print(total)