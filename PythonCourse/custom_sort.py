import time
ALGO_BUBBLE_SORT = 'bubble'
ALGO_INSERTION_SORT = 'insertion'
ALGO_SELECTION_SORT = 'selection'
ALGO_QUICK_SORT = 'quick'
SORT_METHOD_ASC = 'asc'
SORT_METHOD_DESC = 'desc'


class BubbleSort:
    def ascending_order(self, lis):
        start_time = time.time()
        lis_length = len(lis)
        for i in range(lis_length-1):
            for j in range(0, lis_length-i-1):
                if lis[j] > lis[j+1]:
                    lis[j], lis[j+1] = lis[j+1], lis[j]
        end_time = time.time()
        print(f"Ascending sort time: {end_time - start_time} sec")
        return lis

    def descending_order(self, lis):
        start_time = time.time()
        lis_length = len(lis)
        for i in range(lis_length - 1):
            for j in range(0, lis_length-i-1):
                if lis[j] < lis[j + 1]:
                    lis[j], lis[j + 1] = lis[j + 1], lis[j]
        end_time = time.time()
        print(f"Descending sort time: {end_time - start_time} sec")
        return lis


class InsertionSort:
    def ascending_order(self, lis):
        start_time = time.time()
        for i in range(1, len(lis)):
            temp = lis[i]
            j = i-1
            while j >= 0 and lis[j] > temp:
                lis[j+1] = lis[j]
                j -= 1
            lis[j+1] = temp
        end_time = time.time()
        print(f"Ascending sort time: {end_time - start_time} sec")
        return lis

    def descending_order(self, lis):
        start_time = time.time()
        for i in range(1, len(lis)):
            temp = lis[i]
            j = i-1
            while j >= 0 and lis[j] < temp:
                lis[j+1] = lis[j]
                j -= 1
            lis[j+1] = temp
        end_time = time.time()
        print(f"Descending sort time: {end_time - start_time} sec")
        return lis


class SelectionSort:
    def ascending_order(self, lis):
        start_time = time.time()
        for i in range(len(lis)):
            minimum = lis[i]
            for j in range(i+1, len(lis)):
                if lis[j] < minimum:
                    minimum = lis[j]
            temp = lis.index(minimum)
            lis[i], lis[temp] = lis[temp], lis[i]
        end_time = time.time()
        print(f"Ascending sort time: {end_time - start_time} sec")
        return lis

    def descending_order(self, lis):
        start_time = time.time()
        for i in range(len(lis)):
            maximum = lis[i]
            for j in range(i + 1, len(lis)):
                if lis[j] > maximum:
                    maximum = lis[j]

            temp = lis.index(maximum)
            lis[i], lis[temp] = lis[temp], lis[i]
        end_time = time.time()
        print(f"Descending sort time: {end_time - start_time} sec")
        return lis


class QuickSort:
    def partition_asc(self,lis, lb, ub):
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

    def quick_sort_asc(self,lis, lb, ub):
        if lb < ub:
            pivot_position = self.partition_asc(lis, lb, ub)
            self.quick_sort_asc(lis, lb, pivot_position - 1)
            self.quick_sort_asc(lis, pivot_position + 1, ub)
        return lis

    def ascending_order(self,lis):
        start_time = time.time()
        lis = self.quick_sort_asc(lis, 0, len(lis) - 1)
        end_time = time.time()
        print(f"Ascending sort time: {end_time - start_time} sec")
        return lis

    def partition_desc(self,lis, lb, ub):
        start = lb
        end = ub
        while start < end:
            while lis[start] >= lis[lb]:
                start += 1
            while lis[end] < lis[lb]:
                end -= 1
            if start < end:
                lis[start], lis[end] = lis[end], lis[start]
        lis[lb], lis[end] = lis[end], lis[lb]
        return end

    def quick_sort_desc(self,lis, lb, ub):
        if lb < ub:
            pivot_position = self.partition_desc(lis, lb, ub)
            self.quick_sort_desc(lis, lb, pivot_position - 1)
            self.quick_sort_desc(lis, pivot_position + 1, ub)
        return lis

    def descending_order(self,lis):
        start_time = time.time()
        lis = self.quick_sort_desc(lis, 0, len(lis) - 1)
        end_time = time.time()
        print(f"Descending sort time: {end_time - start_time} sec")
        return lis


def sort(lis, algo=ALGO_BUBBLE_SORT, sort_method=SORT_METHOD_ASC):
    # if algo == ALGO_BUBBLE_SORT:
    #     b1 = BubbleSort()
    #     #return b1.ascending_order(lis) if sort_method == SORT_METHOD_ASC else b1.descending_order(lis)
    #
    # elif algo == ALGO_INSERTION_SORT:
    #     b1 = InsertionSort()
    #     #return i1.ascending_order(lis) if sort_method == SORT_METHOD_ASC else i1.descending_order(lis)
    #
    # else:
    #     b1 = SelectionSort()
    #     #return s1.ascending_order(lis) if sort_method == SORT_METHOD_ASC else s1.descending_order(lis)
    # return b1.ascending_order(lis) if sort_method == SORT_METHOD_ASC else b1.descending_order(lis)

    dic = {ALGO_BUBBLE_SORT: 'BubbleSort()', ALGO_SELECTION_SORT: 'SelectionSort()', ALGO_INSERTION_SORT: 'InsertionSort()', ALGO_QUICK_SORT:'QuickSort()'}
    return eval(f"{dic[algo]}.ascending_order({lis}) if sort_method == SORT_METHOD_ASC else {dic[algo]}.descending_order({lis})")
    #
    # dic = {'bubble_asc': 'BubbleSort().ascending_order(lis)', 'bubble_desc':'BubbleSort().descending_order(lis)',
    #        'selection_asc': 'SelectionSort().ascending_order(lis)', 'selection_desc': 'SelectionSort().descending_order(lis)',
    #        'insertion_asc': 'InsertionSort().ascending_order(lis)', 'insertion_desc': 'InsertionSort().descending_order(lis)'}
    # return eval(dic[algo+'_'+sort_method])
