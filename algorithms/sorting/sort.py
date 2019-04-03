def insertion_sort(number_array):
    print("=====Insertion Sort=====")

    for i in range(1, len(number_array), 1):        
        key = number_array[i]        
        j = i - 1
        while j>=0 and number_array[j]>key:
            number_array[j+1] = number_array[j]
            j = j - 1 
        number_array[j+1] = key
    return number_array


def bubble_sort(number_array):
    print("=====Bubble Sort=====")

    for i in range(0, len(number_array), 1):
        for j in range(i+1, len(number_array), 1):
            if number_array[i] > number_array[j]:
                temp = number_array[i]
                number_array[i] = number_array[j]
                number_array[j] = temp
    return number_array

