def is_sorted(arr):
    return arr == sorted(arr) or arr == sorted(arr, reverse=True)
a=[11,343,21,45,76]
print(is_sorted(a))  