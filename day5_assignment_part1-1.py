#Write a function that computes and prints all of the divisors of a user inputted number

def print_factors(my_num):
    current_num = my_num
    while current_num > 0:
        if my_num%current_num == 0:
            print(my_num/current_num)
        current_num -= 1
    print('that is all folks!')
