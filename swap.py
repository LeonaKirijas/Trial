def number_to_string(number):
    if number == 0:
        return "zero"
    elif number == 1:
        return "one"
    elif number == 2:
        return "two"
    elif number == 3:
        return "three"
    else:
        return "Invalid number"

def swap_numbers(a, b):
    a_str = number_to_string(a)
    b_str = number_to_string(b)
    print(f"Before swapping: a = {a_str}, b = {b_str}")
    a, b = b, a
    a_str = number_to_string(a)
    b_str = number_to_string(b)
    print(f"After swapping: a = {a_str}, b = {b_str}")
