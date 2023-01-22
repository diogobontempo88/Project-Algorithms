def merge_sort(word, start=0, end=None):
    if end is None:
        end = len(word)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(word, start, mid)
        merge_sort(word, mid, end)
        merge(word, start, mid, end)
    return word


def merge(word, start, mid, end):
    left = word[start:mid]
    right = word[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            word[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            word[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            word[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            word[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    # if first_string == "" or second_string == "":
    #    return False
    first_order = list(first_string.lower().replace(" ", ""))
    second_oder = list(second_string.lower().replace(" ", ""))

    first_lista = merge_sort(first_order, 0, len(first_order))
    second_lista = merge_sort(second_oder, 0, len(second_oder))

    first_join = "".join(first_lista)
    second_join = "".join(second_lista)

    return (first_join, second_join, first_lista == second_lista)


first_string = ""
second_string = "A"
print(is_anagram(first_string, second_string))
