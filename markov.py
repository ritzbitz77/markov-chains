from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # with open("green-eggs.txt") as file_path:
    #     poem_section = file_path.read()
    poem_section = open("green-eggs.txt").read()   
   
    #variable to assign to string = file_path.read

    # file_path.open(green+eggs.txt)

    return poem_section


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    text_string = open("green-eggs.txt").read() 

    chains = {}

    word = text_string.split()

    for text in range(len(word) - 2):
        first_two_words = (word[text], word[text + 1])
        next_word = word[text+ 2] 

        if first_two_words not in chains:
            chains[first_two_words] = []
    
        chains[first_two_words].append(next_word)

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""


    #link  - key from dictionary and a random word
    # make a key out of second word of first key

    text = ""

    key = choice(chains.keys())
    # words = [key[0], key[1]]
    text = key[0]
    while key in chains:
        text = text + " " + key[1]
        random_words = choice(chains[key])
        key = (key[1], random_words)


    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
