from sort import Sort


class SelectionSort(Sort):

    def __init__(self):
        super(SelectionSort, self).__init__()

    def sort(self, arr):
        for index_i in range(len(arr)):
            min_index = index_i
            for index_j in range(index_i + 1, len(arr)):
                yield index_i, min_index, index_j
                # yield (index_i, 'orange'), (min_index, 'red'), (index_j, 'red')
                if arr[min_index] > arr[index_j]:
                    min_index = index_j
            self.swap(arr, index_i, min_index)
            yield arr

    def __call__(self):
        return SelectionSort.sorting_object
