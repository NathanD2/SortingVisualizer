from sort import Sort
import time


class BruteForceSort(Sort):

    @classmethod
    def sort(cls, arr):
        for i in range(0, len(arr) - 1):
            for j in range(i, len(arr)):
                yield i, j
                if arr[i] > arr[j]:
                    BruteForceSort.swap(arr, i, j)
                yield arr
        yield arr

    @classmethod
    def swap(cls, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

def main():
    delay = .1
    arr = [1, 23, 5, 7, 2, 12, 9]
    print(f"Array before sort: {arr}")
    result = None
    for iteration in BruteForceSort.sort(arr):
        print(iteration)
        result = iteration
        time.sleep(delay)
    print(f"Array after sort: {result}")


if __name__ == '__main__':
    main()