def list_sum_recursive(input_list):
    # Base case
    if input_list == []:
        return 0

    # Recursive case
    # Decompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure
    # and can be defined in terms of a smaller version of itself
    head = input_list[0]
    smaller_list =input_list[1::]
    return head+list_sum_recursive(smaller_list)

print(list_sum_recursive([1, 2, 3]))