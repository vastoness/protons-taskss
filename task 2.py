def remove_extremes(sorted_list, n):
    if n < 0 or n * 2 > len(sorted_list):
        print("invalid value of n") 
    new_list = sorted_list[n:-n]
    return new_list
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 2
print(remove_extremes(sorted_list, n))
