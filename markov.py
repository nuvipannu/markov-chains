# import sys 


#green_eggs = open(green_file_path)



def word_list(green_file_path):
    green_eggs = open(green_file_path)
   
    use_all_text = green_eggs.read() #instead of looping through each line 
    string_text = use_all_text.split() #splits on all whitespace

    # for line in green_eggs:
    # #     line_data = line.rstrip().split(" ")
    # #     file_text_list.extend(line_data)
    
   


    bituple = []
    for i in range(len(string_text)-1):
        word_dict = {}
        word_dict.keys([string_text[i]])
        word_dict.values([string_text[i + 1]])
        i += 2 
        print word_dict

word_list("green-eggs.txt")

# def make_chains(green_file_path):
#  """Takes input text as string; returns dictionary of markov chains."""
#     bituple_list = file_text_list[0] + file_text_list[1]
#     print bituple_list


# make_chains("green-eggs.txt")


#return {} #each bi gram








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



