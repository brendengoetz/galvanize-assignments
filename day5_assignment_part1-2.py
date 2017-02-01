#Write a function that computes the least common multiple between two user inputted numbers.

def find_lcm(x, y):
    bigger_num = max(x, y)
    while(True):
        if bigger_num%x == 0 and bigger_num%y == 0:
            print('The LCM is ') + str(bigger_num)
            break
        bigger_num += 1
