def sort(array):
    n = len(array)
    if n == 1:
        return array
    if n == 2: 
        if array[0] > array[1]:
            array = array[::-1]
        return array
    n >>= 1
    return merge(sort(array[:n]), sort(array[n:]))

def merge(array_a, array_b):
    array = []
    while array_a != [] and array_b != []:
        if array_a[0] < array_b[0]: 
            array.append(array_a[0])
            array_a.pop(0)
        else:
            array.append(array_b[0])
            array_b.pop(0)
    return array + array_a + array_b