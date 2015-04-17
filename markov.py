import sys
import random 

# filepath = open('green-eggs.txt')

def make_chains_func(corpus):
    """Takes input text as string; returns dictionary of markov chains."""
    markov_dictionay = {}


    input_text = corpus
    words_list = input_text.split()

    for i in range(len(words_list) - 2):
        key = (words_list[i], words_list[i + 1])
        value =  words_list[i + 2]
        if key not in markov_dictionay:
            markov_dictionay[key] = [value]
        else:
            markov_dictionay[key].append(value)
        
    return markov_dictionay


def create_text(dictionary):
    """Takes input dictionary and returns a chain of text created from dictionary."""

    #Step 1. Pick a random key"""
    current_randkey = random.choice(dictionary.keys())
    # print current_randkey


    # Step 2. Put that key words in a list/ or create a string

    word_list = [current_randkey[0], current_randkey[1]]
    # print word_list
     
    # Step 3. while key in dict

    while current_randkey in dictionary:
    # # # Step 4. Choose a random value from key 
        value = random.choice(dictionary[current_randkey])
        # print value
    # Step 5. Add that value to that list of words
        word_list.append(value)

        # print word_list

    # Step 6. Make a new key from the second word of current key and value word just choosen
        current_randkey = (current_randkey[1], value)  

    # Step 7. Once the while loop exits, print out all the words (string) 
        
    return " ".join(word_list)

input_path = sys.argv[1]
input_text = open(input_path).read()

#Get a markov chain

the_dictionary = make_chains_func(input_text)


# Produce random text
random_text = create_text(the_dictionary)
print random_text