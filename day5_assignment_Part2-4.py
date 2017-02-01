# Takes an inputted list and returns the total of those numbers multiplied together
def multiply_list(x):
    total = 1
    for num in x:
        total *= num
    return total
