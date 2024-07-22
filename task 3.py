def cumsum(numbers):
    cumsum_list = []
    total = 0  
    for number in numbers:
        total += number
        cumsum_list.append(total)  
    return cumsum_list
numbers = [1, 2, 3, 11]
print(cumsum(numbers)) 
