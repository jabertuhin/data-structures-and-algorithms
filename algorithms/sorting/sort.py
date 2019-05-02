from typing import List, Union


def insertion_sort(array: List[Union[int, float]]) -> List[Union[int, float]]:
    print("=====Insertion Sort=====")

    for i in range(1, len(array), 1):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array


def bubble_sort(number_array: List[Union[int, float]]) -> List[Union[int, float]]:
    print("=====Bubble Sort=====")

    for i in range(0, len(number_array), 1):
        for j in range(i + 1, len(number_array), 1):
            if number_array[i] > number_array[j]:
                temp = number_array[i]
                number_array[i] = number_array[j]
                number_array[j] = temp
    return number_array
