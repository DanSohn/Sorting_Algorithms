# Time Complexity: O(n**2)
# Space Complexity: O(1)
import random


def bubble_sort(A):
    # Bubble sort: go through with multiple passes and compare neighbours, and switch if necessary
    switched = True
    while switched:
        switched = False
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                switched = True


def main():
    A = [x for x in range(1,101)]
    random.shuffle(A)
    print(A)
    bubble_sort(A)
    print(A)


if __name__ == "__main__":
    main()
