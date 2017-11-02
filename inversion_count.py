filename = "array.txt"
inFile = open(filename, 'r')
num_list = list()
for line in inFile:
    num_list.append(int(line))

counts = 0
def inversions_count(array):
    global counts
    mid = round(len(array) / 2)
    left = array[:mid]
    right = array[mid:]
    if len(array) > 1:
        inversions_count(left)
        inversions_count(right)
        i, j = 0, 0
        for k in range(len(left) + len(right) + 1):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
                if i == len(left) and j != len(right):
                    while j != len(right):
                        k += 1
                        array[k] = right[j]
                        j += 1
                    break
            elif left[i] > right[j]:
                array[k] = right[j]
                counts += (len(left) - i)
                j += 1
                if j == len(right) and i != len(left):
                    while i != len(left):
                        k += 1
                        array[k] = left[i]
                        i += 1
                    break
    return counts


# TEST CASES
print('Test result:', inversions_count([5, 2, 3, 4, 5]), '---', 'Expected result:', 3)
print('Test result:', inversions_count([5, 4, 3, 2, 1]), '---', 'Expected result:', 13)
print(inversions_count(num_list))

