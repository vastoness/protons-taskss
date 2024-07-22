mylist = ["bananas" , "oranges" , "apples", "lemons" ]

def list_with_and(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    else:
        formatted_list = ", ".join(items[:-1]) + " and " + items[-1]
        return formatted_list
formatted_string = list_with_and(mylist)
    
print(formatted_string)
