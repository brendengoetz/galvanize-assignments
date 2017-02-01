
#Part 1
# Write a script that prompts the user to input numbers separated by commas.
# Your script will then take these inputted numbers and store them as a list of tuples, two at a time.
# Finally, your script will print that list of tuples to the user.
# If the user inputs an odd number of numbers, then only make a list of the largest number of pairs of two that are possible.
user_input = raw_input('Dear Friend: Enter a list of numbers separated by commas ').split(',')
tuple_list = zip(user_input[::2], user_input[1::2])
print tuple_list

#Part 2.1
user_input = raw_input("Enter a list of numbers separate by '-': " ).split('-')
dct = {}
for item in user_input:
    dct[int(item)] = int(item)**2
print dct

#Part 2.2
user_input = (raw_input("Enter a state and we'll tell you the capital: ")).capitalize()
state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento',
                      'Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                      'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}
for state, capital in state_dictionary.items():
    if user_input == state:
        print 'The captial is', capital
        break
else:
    print "We don't know the capital. Sorry."


#Part 2.3
dct = {}
while True:
    user_input = raw_input("Enter two coordinates and a word separated by commas - x, y, word: ") #user_input is str
    clean = user_input.split(',') #clean is list
    if user_input == '':
        break
    else:
        key = str(clean[0]) + ',' + str(clean[1])
        value = clean[2]
        dct[key] = value
second_input = raw_input("Now enter some coordinates in an x,y format to see what's there: ")
print dct[second_input]

#Part 3.1
user_input1 = raw_input("Enter a list of numbers separated by commas: ").split(',') #user_input is list
user_input2 = raw_input("Enter another list of numbers separated by commas: ").split(',') #user_input is list
set1 = set(user_input1)
set2 = set(user_input2)
print set1.intersection(set2)

#Part 3.2
user_input1 = raw_input("Enter a list of words separated by commas: ").split(',') #user_input is list
set1 = set(user_input1)
print set1


#Part 3.3
lst = set([])
while True:
    user_input = raw_input('Enter a word to add to the vocab: ')
    if user_input == 'v':
        print lst
    elif user_input == 'q':
        break
    else:
        lst.add(user_input)
