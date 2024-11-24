

def quicksort(arr):
    if (len(arr) <= 1):
        return arr
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if (x < pivot)]
    equal_to_pivot = [x for x in arr if (x == pivot)]
    greater_than_pivot = [x for x in arr[1:] if (x > pivot)]
    return ((quicksort(less_than_pivot) + equal_to_pivot) + quicksort(greater_than_pivot))
