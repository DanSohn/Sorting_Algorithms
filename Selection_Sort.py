# Time complexity: O(n^2) since the two nested for loop
# Space complexity: O(1), since I don't use any extra data structures, I do everything in place
import random


def selection_sort(A):
    for sorted_i in range(len(A)):
        curr_min_index = sorted_i
        for unsorted_i in range(sorted_i, len(A)):
            if A[unsorted_i] < A[curr_min_index]:
                curr_min_index = unsorted_i
        A[sorted_i], A[curr_min_index] = A[curr_min_index], A[sorted_i]


def main():
    A = [x for x in range(1, 101)]
    random.shuffle(A)
    print(A)
    selection_sort(A)
    print(A)


if __name__ == "__main__":
    main()