#Assignment for Day 2

#1
my_num = (int(input('My number is: ')))
if my_num > 0:
    print('The inputted number is Positive!')
elif my_num < 0:
    print('The inputted number is Negative! Too bad :(')
elif my_num == 0:
    print('The inputted number is Zero. Crazy!')

#2
first_num = int(input('My first number is: '))
second_num = int(input('My second number is: '))
if first_num > second_num:
    print('The first number is bigger, bitch.')
else:
    print ('The second number is bigger, bitch.')

#3
my_num = int(input('Enter a number to find the sum down from: '))
sum_result = 0
current = my_num
while current >= 0:
    sum_result += current
    current -= 1
print(sum_result)

#4
my_num = int(input('You want a factorial? Enter a number bitch: '))
sum_result = 1
current = my_num
while current > 0:
    sum_result *= current
    current -= 1
print(sum_result)

#5
my_num = int(input('Print factors for this number:'))
current_num = my_num
while current_num > 0:
    if my_num%current_num == 0:
        print(my_num/current_num)
    current_num -= 1
print('that is all folks!')

#6
my_first_num = int(input('My first number is:'))
my_second_num = int(input('My second number is:'))
current_num = min(my_first_num, my_second_num)
lower_num = min(my_first_num, my_second_num)
bigger_num = max(my_first_num, my_second_num)

while current_num > 0:
    if lower_num%current_num == 0:
        if bigger_num%current_num == 0:
            print('The greatest common denominator is ') + str(current_num)
            break
    current_num -= 1

#7
my_first_num = int(input('My first number is:'))
my_second_num = int(input('My second number is:'))
bigger_num = max(my_first_num, my_second_num)

while(True):
    if bigger_num%my_first_num == 0 and bigger_num%my_second_num == 0:
        print('The LCM is ') + str(bigger_num)
        break
    bigger_num += 1

#8
my_num = int(input('Tell me if this number is prime: '))
current_num = 2
prime = True
while current_num <= my_num**0.5:
    if my_num%current_num == 0:
        prime = False
    current_num += 1
if prime:
    print('Your number is prime, you smarty pants!')
else:
    print('Your number is NOT prime. Nice try though!')

#9
nth_term = int(input('What number element in the series should we compute? '))
element_num = 0
value = 1
while element_num < nth_term:
    value = value * 2 + 1
    element_num += 1
print(value)
