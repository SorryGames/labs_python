def sort(array):
    array.sort()  # to speed up sort-stage
    return array

def _sort(array):
    array = [ [i] for i in array ]
    while len(array) > 1:
        array.append(merge(array[0], array[1]))
        array.pop(0); array.pop(0)
    return array[0]

def _merge(array_a, array_b):
    array = []
    i, j = 0, 0
    while i < len(array_a) and j < len(array_b):
        if array_a[i] < array_b[j]: 
            array.append(array_a[i])
            i += 1
        else:
            array.append(array_b[j])
            j += 1
    #
    while i < len(array_a):
        array.append(array_a[i])
        i += 1
    while j < len(array_b):
        array.append(array_b[j])
        j += 1
    #
    return array