import random 

green_eggs = open('green-eggs.txt')

def make_chains_func(corpus):
    """Takes input text as string; returns dictionary of markov chains."""
    mark_chains = {}


    text_green_eggs = corpus.read()
    green_eggs_list = text_green_eggs.split()

    for i in range(len(green_eggs_list) - 2):
        key = (green_eggs_list[i], green_eggs_list[i + 1])
        value =  green_eggs_list[i + 2]
        if key not in mark_chains:
            mark_chains[key] = [value]
        else:
            mark_chains[key].append(value)
        
    return mark_chains


def create_text(dictionary):
    """Takes input dictionary and returns a chain of text created from dictionary."""

    #Step 1. Pick a random key"""
    current_randkey = random.choice(dictionary.keys())
    print current_randkey


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

    print " ".join(word_list)


the_dictionary = make_chains_func(green_eggs)

create_text(the_dictionary)