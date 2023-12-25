def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(element, arr):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

    return -1
unsorted_list = [64, 34, 25, 12, 22, 11, 90]


sorted_list = bubble_sort(unsorted_list.copy())
print("Sorted list (bubble sort method):", sorted_list)

element_to_search = 2
index = binary_search(element_to_search, sorted_list)

if index != -1:
    print(f"Element {element_to_search} found at index {index}.")
else:
    print(f"Element {element_to_search} not found.")
