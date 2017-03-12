# -*- coding: utf-8 -*-
"""
@Time    : 3/3/17 11:14 AM
@Author  : zcj
"""


# 平均时间复杂度O(n^2),空间代价O(1),稳定排序
def insert_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
    return array


# 平均时间复杂度O(n^2),空间代价O(1),稳定排序
def bin_insert_sort(arr):
    for i in range(1, len(arr)):
        left = 0
        right = i - 1
        key = arr[i]
        while left <= right:
            mid = (left + right) / 2
            if arr[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        j = i - 1
        while j >= left:
            arr[j + 1] = arr[j]
            j -= 1
        arr[left] = key
    return arr


# 不占用内存，稳定排序，时间复杂度O(n^2)
def bubble_sort(arr):
    count = len(arr)
    while count > 0:
        for j in range(count - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        count -= 1
        print arr
    return arr


# 不稳定算法，时间复杂度O(n^2),不占用内存
def select_sort(arr):
    for i in range(len(arr)):
        min_value = i
        for j in range(i + 1, len(arr)):
            if arr[min_value] > arr[j]:
                min_value = j
        arr[min_value], arr[i] = arr[i], arr[min_value]
    return arr


# 平均时间复杂度nlog(n),最差时间复杂度O(n^2),不稳定排序
def quick_sort(lists, left, right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


# 时间复杂度O(n^2)
def shell_sort(arr):
    step = 2
    count = len(arr)
    group = count / step
    while group > 0:
        for i in range(group):
            j = i + group
            while j < count:
                k = j - group
                key = arr[j]
                while k >= 0 and arr[k] > key:
                    arr[k + group] = arr[k]
                    k -= group
                arr[k + group] = key
                j += group
        group /= step
    return arr


def bubble_sort1(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                flag = True
        n -= 1
    return arr


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


# 稳定排序，时间复杂度nlog(n),占用内存
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    num = len(arr) / 2
    left = merge_sort(arr[:num])
    right = merge_sort(arr[num:])
    return merge(left, right)

pass
ll = [5, 6, 2, 7, 9, 3, 1, 4, 8, 10, 0]
li = merge_sort(ll)
print li
