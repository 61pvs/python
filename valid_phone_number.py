import re

N = int(input())
regex_pattern = r"^(7|8|9)([0-9]){9}$"

for _ in range(N):
    if re.match(regex_pattern, input()):
        print('YES')
    else:
        print("NO")