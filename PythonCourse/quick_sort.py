

def partition(lis, lb, ub):
    start = lb
    end = ub
    while start < end:
        while lis[start] <= lis[lb]:
            start += 1
        while lis[end] > lis[lb]:
            end -= 1
        if start < end:
            lis[start], lis[end] = lis[end], lis[start]
    lis[lb], lis[end] = lis[end], lis[lb]
    return end


def quick_sort(lis, lb, ub):
    if lb < ub:
        pivot_position = partition(lis, lb, ub)
        quick_sort(lis, lb, pivot_position-1)
        quick_sort(lis, pivot_position+1, ub)
    return lis


lis = [23, 5, 6, 12, 4, 34, 89, 56, 8, 9, 10, 40, 30, 0]
sorted_list = quick_sort(lis, 0, len(lis)-1)
print(f"Ascending Sorted List:{sorted_list}")
