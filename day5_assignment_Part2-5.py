#Takes an inputted list and returns a list of the even numbers
def my_list(x):
    evens_list = []
    for num in x:
        if num % 2 == 0:
            evens_list.append(num)
    return evens_list
