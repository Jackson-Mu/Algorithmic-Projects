#=================================================================================================
# Name         : SelectionSortGame
# Author       : Jackson Mukeshimana
# Version      : 01
# Date Created : 12/02/2024
# Date Modified: 12/02/2024
# Description  : Selection Sort Algorithm for Sorting Computer File names in Python language
#=================================================================================================

def merge_sort(file_names):
    # Check if the length of the file_names list is greater than 1
    if len(file_names) > 1:
        mid = len(file_names) // 2
        left_half = file_names[:mid]
        right_half = file_names[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                file_names[k] = left_half[i]
                i += 1
            else:
                file_names[k] = right_half[j]
                j += 1
            k += 1

        # Copy the remaining elements from left_half
        while i < len(left_half):
            file_names[k] = left_half[i]
            i += 1
            k += 1

        # Copy the remaining elements from right_half
        while j < len(right_half):
            file_names[k] = right_half[j]
            j += 1
            k += 1
 #For testing our above implemented Merge Sort Algorithm 
file_names = ["file3.txt", "file1.txt", "file2.txt","file3.txt", "file4.txt", "file5.txt", "file6.txt"] 
merge_sort(file_names)
print("Sorted file names:", file_names)

