import custom_sort
lis = [23, 5, 6, 12, 4, 34, 89, 56, 8, 9, 10, 40, 30, 0]
new_list = custom_sort.sort(lis, algo=custom_sort.ALGO_BUBBLE_SORT, sort_method=custom_sort.SORT_METHOD_ASC)
print(f"Bubble sorted Ascending list: {new_list}")
print(f"Bubble sorted Descending list: {custom_sort.sort(lis, algo=custom_sort.ALGO_BUBBLE_SORT, sort_method=custom_sort.SORT_METHOD_DESC)}")

new_list_insertion = custom_sort.sort(lis, algo=custom_sort.ALGO_INSERTION_SORT, sort_method=custom_sort.SORT_METHOD_ASC)
print(f"Insertion_sorted Ascending list: {new_list_insertion}")
print(f"Insertion sorted Descending list: {custom_sort.sort(lis, algo=custom_sort.ALGO_INSERTION_SORT, sort_method=custom_sort.SORT_METHOD_DESC)}")

new_list_selection = custom_sort.sort(lis, algo=custom_sort.ALGO_SELECTION_SORT, sort_method=custom_sort.SORT_METHOD_ASC)
print(f"Selection sorted Ascending list: {new_list_selection}")
print(f"Selection sorted Descending list: {custom_sort.sort(lis, algo=custom_sort.ALGO_SELECTION_SORT, sort_method=custom_sort.SORT_METHOD_DESC)}")

new_list_quick = custom_sort.sort(lis, algo=custom_sort.ALGO_QUICK_SORT, sort_method=custom_sort.SORT_METHOD_ASC)
print(f"Quick sorted Ascending List: {new_list_quick}")
print(f"Quick sorted Descending list: {custom_sort.sort(lis, algo=custom_sort.ALGO_QUICK_SORT, sort_method=custom_sort.SORT_METHOD_DESC)}")
