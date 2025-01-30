import timeit
import random

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

numbers = [5, 3, 8, 4, 2]
insertion_sort(numbers)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def timsorted(array):
    return sorted(array)


def timsort(array):
    return array.sort()

def generate_dataset(length):
    return [random.randint(0, length) for _ in range(length)]

def time_measurement(length):
    print(f"Test for '{length}' elements:")
    execution_time = timeit.timeit(lambda: insertion_sort(generate_dataset(length)), number=1)
    print(f"Time for insertion_sort: {execution_time}")
    execution_time = timeit.timeit(lambda: merge_sort(generate_dataset(length)), number=1)
    print(f"Time for merge_sort: {execution_time}")
    execution_time = timeit.timeit(lambda: timsorted(generate_dataset(length)), number=1)
    print(f"Time for timsorted: {execution_time}")
    execution_time = timeit.timeit(lambda: timsort(generate_dataset(length)), number=1)
    print(f"Time for timsort: {execution_time}")

time_measurement(100)
time_measurement(1000)
time_measurement(10000)