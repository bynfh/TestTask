import random

lists = []
# Create some lists in list
for i in range(11):
    lists.append([random.randint(1, 100) for numb in range(10)])


def merge(first_list, second_list):
    """
    Compare element in two list and return result in order
    Takes two list
    return list

    """
    merged_list = []
    if len(first_list) == 0:
        return second_list
    if len(second_list) == 0:
        return first_list

    index_first, index_second = 0, 0
    while len(merged_list) < len(first_list) + len(second_list):
        if first_list[index_first] <= second_list[index_second]:
            merged_list.append(first_list[index_first])
            index_first += 1
        else:
            merged_list.append(second_list[index_second])
            index_second += 1

        if index_second == len(second_list):
            merged_list += first_list[index_first:]
            break
        if index_first == len(first_list):
            merged_list += second_list[index_second:]
            break
    return merged_list


def merge_sort(unsorted_list):
    """
    Recursion function
    Splits input list into two parts and calls function merge
    Takes list
    return sorted list

    """
    if len(unsorted_list) < 2:
        return unsorted_list
    middle = len(unsorted_list) // 2
    return merge(first_list=merge_sort(unsorted_list[:middle]),
                 second_list=merge_sort(unsorted_list[middle:]))


print("=="*10, "Start testing".upper(), "=="*10)

for unsorted_list in lists:
    sorted_list = merge_sort(unsorted_list)
    print(f"Unsorted list:{unsorted_list}\n  Sorted list:{sorted_list}\n")
    assert sorted_list == sorted(unsorted_list), "PRIVET"

print("=="*10, f"Tests finished".upper(), "=="*10)
