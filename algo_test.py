import algorithms.sorting as algo_sort

number_list = [90, 8923, 24, 3245, 2, 234, 32, 22, 254, 234, 2345, 214, 2, 4, 62, 64, 67]
print("Unsorted Number List -> ", end='')
print(number_list)
# --------- insertion sort -----------
print(algo_sort.insertion_sort(number_list))
print("="*50)

