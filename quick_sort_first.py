
def partition(A, l, r):
    p = A[l]
    i = l + 1
    for j in range(l+1, r):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i = i + 1
    A[l], A[i-1] = A[i-1], A[l]
    return i - 1


def quick_sort(A, l, r):
    count = 0
    if r - l <= 1:
        return 0
    else:
        split = partition(A, l, r)
        count = r - l - 1
        l_count = quick_sort(A, l, split)
        r_count = quick_sort(A, split+1, r)
        return count + l_count + r_count

filename = "quicksort.txt"
inFile = open(filename, 'r')
x = list()
for line in inFile:
    x.append(int(line))
print(quick_sort(x, 0, len(x)))

