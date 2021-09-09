current_number = 1
accumlated_sum = 0

def sum_recursive():
    global current_number
    global accumlated_sum

    # Base Case
    if current_number == 11:
        return accumlated_sum
    else:
        accumlated_sum = accumlated_sum+current_number
        current_number= current_number+1
        return sum_recursive()

print(sum_recursive())