# -*- coding: utf-8 -*-
"""
@Time    : 3/3/17 11:14 AM
@Author  : zcj
"""
import random


def random_num(num):
    arr = []
    i = 1
    while i < num:
        arr.append(random.randint(0, 10000))
        i += 1
    return arr


def insert_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
    return array


def bubble_sort(arr):
    count = len(arr)
    for i in range(count):
        for j in range(i + 1, count):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def select_sort(arr):
    for i in range(len(arr)):
        min_value = i
        for j in range(i + 1, len(arr)):
            if arr[min_value] > arr[j]:
                min_value = j
        arr[min_value], arr[i] = arr[i], arr[min_value]
    return arr


def quick_sort(arr, left, right):
    if left >= right:
        return arr
    key = arr[left]
    low = left
    high = right
    while left < right:
        while left < right and arr[right] >= key:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= key:
            left += 1
        arr[right] = arr[left]
    arr[right] = key
    quick_sort(arr, low, left - 1)
    quick_sort(arr, left + 1, high)
    return arr


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        result += left[i:]
        result += right[j:]
        return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    num = len(arr) / 2
    left = merge_sort(arr[:num])
    right = merge_sort(arr[num:])
    return merge(left, right)

ll = [5, 6, 2, 7, 9, 3, 1, 4, 8, 10, 0]
arr = random_num(10)
li = quick_sort(arr, 0, len(arr) - 1)
print li
