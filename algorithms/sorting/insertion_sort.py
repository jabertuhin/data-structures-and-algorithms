def insertion_sort(number_array):

    for i in range(1, len(number_array), 1):        
        key = number_array[i]        
        j = i - 1
        while j>=0 and number_array[j]>key:
            number_array[j+1] = number_array[j]
            j = j - 1 
        number_array[j+1] = key
    return number_array


if __name__ == "__main__":
    number = [99, 19, 90, 3, 34, 2, 234, 23]
    print(insertion_sort(number))