#============================================================================
# Name         : SelectionSort
# Author       : Jackson Mukeshimana
# Version      : 01
# Date Created : 08/02/2024
# Date Modified: 08/02/2024
# Description  : Selection Sort Algorithm implemented in Python language
#============================================================================

# We can start with the array of some elements
A = [1, 3, 9, 7, 4, 5, 10]

# We can first initialize some variables i and j
i = 0
j = 0

# Then we can run the for loop through all those elements
for i in range(len(A) - 1, 0, -1):

    # We then initialize the element that would help us to find the current largest element at every iteration
    m = i

    # We then continue with another loop that will compare elements to elements in the array
    for j in range(i):
        if A[m] < A[j]:
            # Then we update the current maximum element in the list
            m = j

    # Then we swap those two elements, the one greater to come first since we want the largest element to be the first one
    A[m], A[i] = A[i], A[m]

print("The Sorted elements by Selection sort would be the following: ")
for i in range(len(A)):
    print("%d" % A[i], end=", ")
print()  # Printing a new line to separate the output

