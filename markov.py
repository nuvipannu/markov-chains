import sys 
print sys.argv

green_eggs = open('green-eggs.txt')

def make_chains(green_eggs):
    """Takes input text as string; returns dictionary of markov chains."""
mark_chains = {}


text_green_eggs = green_eggs.read()
green_eggs_list = text_green_eggs.split()

for i in range(len(green_eggs_list) - 2):
    key = (green_eggs_list[i], green_eggs_list[i + 1])
    value =  green_eggs_list[i + 2]
   
    if key not in mark_chains:
        mark_chains[key] = []
        
    mark_chains[key].append(value)

print mark_chains



#     #we have the words in a list separately as items and we have created an empty dict
#         #for the length of the list, we want to:
#         #get the [0] term, assign it to key
#         # get the [1] term, assign it to value
#         # get the [1] term, assign to key
#         # get the [2] term, assign to value, etc until the end of the list
#     # for len(green_eggs_list):
#     #     green_eggs_list[0] = key
#     #     green_eggs_list[1] = value
#     #     green_eggs_dict[key] = [value]
#     # return {}

# def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""

#     return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

# input_text = "Some text"

# # Get a Markov chain
# chain_dict = make_chains(input_text)

# # Produce random text
# random_text = make_text(chain_dict)

# print random_text
