n = input()
max_num = -1

for i in range(len(n)):
    new_num = int(n[:i] + n[i+1:])
    if new_num > max_num:
        max_num = new_num

print(max_num)
