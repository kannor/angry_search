'''
output = []
split = True
def count_words(string):
    for char in string:
        if char == " ":
            split = True
        else:
            if split:
                output.append(char)
                split = False
            else:
                output[-1] = output[-1] + char
    return len(output)
                
        
''' 
def count_words(string):
    out = string.split(string)
    print out
    return len(out)


passage =("The number of orderings of the 52 cards in a deck of cards "
"is so great that if every one of the almost 7 billion people alive "
"today dealt one ordering of the cards per second, it would take "
"2.5 * 10**40 times the age of the universe to order the cards in every "
"possible way.")
print count_words(passage)
#>>>56

