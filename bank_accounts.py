from collections import Counter


def print_rez(x):
    c = Counter(x)
    for key, value in sorted(c.items()):
        print('{account} {number}'.format(account=key.strip(), number=value))


num_tests = int(input())
for t in range(num_tests):
    num = input()
    if not num:
        num = input()
    accounts = [input() for i in range(int(num))]
    print_rez(accounts)
