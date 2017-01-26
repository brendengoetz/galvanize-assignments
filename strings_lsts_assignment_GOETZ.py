#A work in progress here. Only have parts 1 and 2 (almost) finished

#in order to un-comment an assignment question script...
#highlight the desired section, then type cmd+/

#warm up 1
#this is just the final version of the script. i did not save the incremental steps along theway
user_input = raw_input('Add this: ')
my_str = 'This String was not Chosen Arbitrarily...'
my_str = my_str + user_input
print my_str

#warm up 2
#this is just the final version of the script. i did not save the incremental steps along theway
user_input = raw_input('Add this to the list: ')
my_list = [1, 'hello', 2, 'there', 3, 'list']
if len(user_input) < 8:
    my_list.append(user_input)
else: my_list.append(4)
print my_list

#warm up 3
#this is just the final version of the script. i did not save the incremental steps along theway
user_number = int(raw_input('Min length to be printed: '))
my_list = ['hello', 'there', 'python', list('list'), '!']
longer_list = []
for element in my_list:
    if len(element) > user_number:
        longer_list.append(element)
    print longer_list

###Assignment begins here
###Written in Python 3.5

## Part 1 - Practice with For Loops

#Sum numbers up to the inputted number
my_num = int(input('Enter a number to find the sum down from: '))
result = 0
for num in range(1, my_num+1):
    result = num + result
print(result)

#Write a script that computes and prints the factorial of a user inputted number.
my_num = int(input('You want a factorial? Enter a number: '))
result = 1
for num in range(1, my_num+1):
    result = result*num
print (result)

#Write a script that determines whether or not a user inputted number is a prime
my_num = int(input('See if this numer is prime: '))
for x in range(2, my_num):
    result = my_num%x
    if result == 0:
        print(str(my_num) + ' is NOT prime')
        break
else:
    print(str(my_num) + ' is a prime')

## Part 2 - Practice with Strings

#1 Write a script that obtains the count of a user inputted letter in a user inputted string
my_str = input('Write something: ').lower()
my_let = input('Now choose a letter from what you wrote: ').lower()
print(my_str.count(my_let))

#2 Write a script that checks if a user inputted string ends in an exclamation point
my_str = input('Write something: ')
if my_str.endswith('!'):
    print(my_str.upper())
else:
    print(my_str.lower())

#3 Write a script that removes all of the vowels in a user inputted string.
my_str = input('Write something: ')
vowels = [ 'a','e','i','o','u']
new = my_str
for char in my_str:
    if char in vowels:
        new = new.replace(char, '')
print(new)

#4 Write a script that makes every other letter of a user inputted string capitalized
Struggling to get this one...
Can have it
my_str = input('Write something: ')
#for char in my_str:
print(my_str[::2].upper())
