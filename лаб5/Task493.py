n, k = map(int, input().split())

pins = ['I'] * n

for _ in range(k):
    m, h = map(int, input().split())
    for i in range(m-1, h):  
        pins[i] = '.'

print(''.join(pins))
