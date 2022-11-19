def findZigZagSequence(a, n):
    a.sort()
    print(a)
    mid = int((n + 1)/2)-1#
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2#
    while(st <= ed):
        print(a, mid, st, ed)
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1#

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

n = 5
a = [1, 4, 3, 2, 5]
findZigZagSequence(a, n)