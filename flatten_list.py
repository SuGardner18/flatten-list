#if there is an empty list exit the function
#Look at each item of the list, pull first item and leave the rest
#if the item is a list then call it again and continue to do so until flatten
#if is a number just add it to list


def flatten_list(lst):
    if lst==[]:
        return []
    first_item = lst[0]
    rest_of_items=lst[1:]
    if isinstance(first_item,list):
        return flatten_list(first_item)+ flatten_list(rest_of_items)
    else:
        return [first_item] + flatten_list(rest_of_items)
    

print(flatten_list([1, 2, [3], [4,5]]))
print(flatten_list([1, [2], [3, [4, 5, [6]]], 7]))