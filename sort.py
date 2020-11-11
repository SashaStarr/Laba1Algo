from model.farm import Farm
from typing import List
from other_result import *

def sort_fan_power_in_watts_des(farm_arr: List[Farm]):
    Result =  Results("Selection alg")
    for number_sort in range(len(farm_arr)):
        min = number_sort
        #comparisons
        for second_number_sort in range(number_sort + 1, len(farm_arr)):
            Result.number_of_comparisons()
            if farm_arr[min].fan_power_in_watts <= farm_arr[second_number_sort].fan_power_in_watts:
                min = second_number_sort
        # swap
        Result.number_of_swaps()
        farm_arr[number_sort], farm_arr[min] = farm_arr[min],farm_arr[number_sort]
    Result.statistic()

def sort_number_of_animals_asc(farm_arr: List[Farm]):
    Result =  Results("QuickSort alg")
    finish = len(farm_arr)
    def separation(farm_arr, low_index, high_index):
        start_index = (low_index - 1)
        last_index = farm_arr[high_index]
        for alg_number in range(low_index, high_index):
            Result.number_of_comparisons()
            if farm_arr[alg_number].number_of_animals <= last_index.number_of_animals:
                start_index += 1
                Result.number_of_swaps()
                farm_arr[start_index], farm_arr[alg_number] = farm_arr[alg_number], farm_arr[start_index]
        Result.number_of_swaps()
        farm_arr[start_index + 1], farm_arr[high_index] = farm_arr[high_index], farm_arr[start_index + 1]
        return (start_index + 1)
    def quick_sort(farm_arr, low_index, high_index):
        Result.number_of_comparisons()
        if low_index < high_index:
            partitioning_index = separation(farm_arr, low_index, high_index)
            quick_sort(farm_arr, low_index, partitioning_index - 1)
            quick_sort(farm_arr, partitioning_index + 1, high_index)
    quick_sort(farm_arr, 0, finish - 1)
    Result.statistic()


def print_array(farm_arr: List[Farm]):
    for element in farm_arr:
        print(element)