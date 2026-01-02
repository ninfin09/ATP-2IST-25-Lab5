numbers = list(map(int, input().split()))

repeated = set()
seen = set()

for x in numbers:
    if x in seen:
        repeated.add(x)
    else:
        seen.add(x)

for x in sorted(repeated):
    print(x, end=" ")
