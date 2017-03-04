# -*- coding: utf-8 -*-
"""
@Time    : 3/3/17 11:14 AM
@Author  : zcj
"""


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

ll = [5, 6, 2, 7, 9, 3, 1, 4, 8, 10, 0]
li = select_sort(ll)
print li
