#=================================================================================================
# Name         : SelectionSortGame
# Author       : Jackson Mukeshimana
# Version      : 01
# Date Created : 12/02/2024
# Date Modified: 12/02/2024
# Description  : Selection Sort Algorithm for Sorting 1980s themed enemy names in Python language
#=================================================================================================

# Function to perform selection sort on a list of elements
def selection_sort(list_array):
    n = len(list_array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if list_array[j] < list_array[min_index]: 
                min_index = j
        list_array[i], list_array[min_index] = list_array[min_index], list_array[i]  # Swapping the elements

# 1980s themed enemy names for testing
enemy_names = ["Terminator", "Robocop", "Predator", "Alien", "Rambo", "Indiana", "Conan", "Rocky", "He-Man", "Skeletor"]
selection_sort(enemy_names)
print("Sorted enemy names:", enemy_names)
