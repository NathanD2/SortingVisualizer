from sort import Sort


class BubbleSort(Sort):

    def __init__(self):
        super(BubbleSort, self).__init__()

    def sort(self, arr):
        while True:
            is_sorted = True
            for index_i in range(len(arr) - 1):
                yield index_i, index_i + 1
                if arr[index_i] > arr[index_i + 1]:
                    self.swap(arr, index_i, index_i + 1)
                    is_sorted = False
                yield arr
            if is_sorted:
                return arr

    def __call__(self):
        return BubbleSort.sorting_object
