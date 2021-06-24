from sort import Sort


class InsertionSort(Sort):

    def __init__(self):
        super(InsertionSort, self).__init__()

    def sort(self, arr):
        for index_i in range(1, len(arr)):
            element = arr[index_i]
            index_j = index_i - 1

            while index_j >= 0 and element < arr[index_j]:
                yield index_i, index_j
                index_j -= 1
            arr.pop(index_i)
            arr.insert(index_j + 1, element)
            yield arr

    def __call__(self):
        return InsertionSort.sorting_object
