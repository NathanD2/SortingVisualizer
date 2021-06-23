from sort import Sort

class BruteForceSort(Sort):

    def __init__(self):
        super(BruteForceSort, self).__init__()

    def sort(self, arr):
        if BruteForceSort.sorting_object is None:
            BruteForceSort.sorting_object = BruteForceSort()
        for i in range(0, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                yield i, j
                if arr[i] > arr[j]:
                    self.swap(arr, i, j)
                yield arr
        yield arr

    def __call__(self):
        return BruteForceSort.sorting_object

# def main():
#     delay = .1
#     arr = [1, 23, 5, 7, 2, 12, 9]
#     print(f"Array before sort: {arr}")
#     result = None
#     for iteration in BruteForceSort.sort(arr):
#         print(iteration)
#         result = iteration
#         time.sleep(delay)
#     print(f"Array after sort: {result}")
#
#
# if __name__ == '__main__':
#     main()
