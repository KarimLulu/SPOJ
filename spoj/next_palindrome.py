def find(n):
    num = str(n)
    length = len(num)
    is_odd = length % 2
    left = num[:length//2]
    middle = num[length//2] if is_odd else ""

    rez = left+middle+left[::-1]
    if rez > num:
        return rez

    if middle and middle < '9':
        middle = str(int(middle)+1)
        return left + middle + left[::-1]
    elif middle:
        middle = '0'

    if all(el=='9' for el in left):
        return '1' + '0'*(len(num)-1) + '1'
    else:
        l = list(left)
        k = len(l)-1
        for i,el in enumerate(l[::-1]):
            if el=='9':
               l[k-i] = '0'
            else:
                l[k-i] = str(int(el)+1)
                break
        left = "".join(l)
        return left + middle + left[::-1]

for k in range(int(input())):
    number=input()
    print(find(number))
