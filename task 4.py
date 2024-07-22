def is_sorted(values):
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True

values = [10, 12, 16, 21, 30]
print(is_sorted(values)) 
values = [1, 3, 2, 4, 5]
print(is_sorted(values))  
