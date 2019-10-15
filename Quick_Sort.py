# Time Complexity:
# Space Complexity:
import random


def quick_sort(A, low, high):
    # low = starting index, high = ending index

    if low < high:
        pivot = partition(A, low, high)

        quick_sort(A, low, pivot-1)
        quick_sort(A, pivot+1, high)


def partition(A, low, high):
    """
    Partition uses the last element as a pivot, and places all elements less than it to its left, and all elements
    greater to its right, and ensures pivot is in the correct index
    :param A: Array to partition
    :param low: starting index
    :param high: ending index
    :return: pivot index
    """
    # pivot VALUE placed at the very right of array
    pivot = A[high]

    i = low
    for j in range(low, high):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[high] = A[high], A[i]
    return i


def main():
    A = [x for x in range(1,101)]
    random.shuffle(A)
    print(A)
    quick_sort(A, 0, len(A)-1)
    print(A)


if __name__ == "__main__":
    main()
