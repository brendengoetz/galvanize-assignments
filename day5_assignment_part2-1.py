'''Write a function that figures out
whether or not we have any beers left on our wall.
It should take in a number,
and then print 'No beers left' if we are at the end
(i.e. there are 0 beers left)
or 'Beers left!' if we are not at the end
(i.e. there are not 0 beers left).'''


# This is a confusingly worded question
# Takes an input of some number and tells us if we have any beer left
def beers_left(n):
    if n > 0:
        print 'Beers left!'
    else:
        print 'No beers left :('
