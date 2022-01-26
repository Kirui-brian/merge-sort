# Merge function
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    # Create arrays
    L = [0]
    R = [0]
    # Copy data to arrays
    for i in range(0, n1):
        L[i] = arr[l + 1]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0  # First half of array
    j = 0  # Second half of array
    k = l  # Merge two halves
    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # Copy the left out elements of the left half
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    # Copy the left out elements of the right half
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# Sort
def mergeSort(arr, l, r):
    if l < r:
        # Getting the average
        m = (l + (r - 1)) / 2
        # Sort
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


# Main
arr = [2, 5, 3, 8, 6, 5, 4, 7]
n = len(arr)
mergeSort(arr, 0, n - 1)
print("Sorted array is: ")
for i in range(n):
    print(arr[i], end=" ")
