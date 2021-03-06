 # update to use with twitter api.  will import this exercise8.py as module
 # and then call main(path) by passing the txt file to use

# from sys import argv
# script, filepath = argv

import random

def file_into_wordlist(path):
    """unpack text file, and place into list of words.  
    each word is a string.  List is ordered.  
    Return word_list"""
    file_obj = open(path)
    read_file = file_obj.read()
    wordlist = read_file.split()
    return wordlist

def create_dictionary(alist,len_of_N):
    """Create a dictionary, with a N-gram as a key, 
    and the value is a list containing words that follow 
    each occurrence of the N-gram in the word_list. 
    N-gram can be of any length specified by len_of_N.
    Returns dictionary."""
    bigram_dict= {}
    for index in range(len(alist)-len_of_N):
        key_as_list = []
        # if N-gram is bigram, len_of_N = 2
        # the value is the third position [2], index+len_of_N
        # the key of this N-gram is position [0] and [1],
        #     which equals len_of_N - 1
        counter = 0
        while counter < len_of_N:
            key_as_list.append(alist[index+counter]) 
            counter += 1
        value = alist[index+len_of_N]
        key = tuple(key_as_list)
        if key not in bigram_dict:
            bigram_dict[key] = [value]
        else:
            bigram_dict[key].append(value)
        index +=1
    return bigram_dict 

def string_generator(adict, max_len):
    """start with an N-gram (one of the keys) from the
    dictionary, and add subsequent words to this string based 
    on random choice from the dictionary. returns a newly
    generated string."""
    # create random key which is constructed from one of the tuple keys
    list_of_keys = adict.keys()
    key = random.choice(list_of_keys)
    output_string = " ".join(key)
    current_len = 0
    while (key in adict) and (current_len < max_len):
        # identify the next word using dictionary
        values_list = adict[key]
        next_word = random.choice(values_list)
        # string together tuple and next word
        output_string = output_string + " " + next_word
        key = key[1:] + (next_word,)
        current_len = len(output_string)
    return output_string


def main(filepath):
    markov_chains = create_dictionary(file_into_wordlist(filepath), 2)
    #print markov_chains
    output = "Testing Markov Chains: "+string_generator(markov_chains, 110)
    print output
    return output

if __name__ == "__main__":
    main("sonnet.txt")

