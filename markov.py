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

    text = open("green-eggs.txt").read() 

    chains = {}


    for word in range(len(text) - 1):
        word = text.split()
        for word in text:
            return "%s, %s" %(text[0], text[0 + 1])
        

        # word = text.split()
        # word1 = text[0]
        # word2 = text[1]
        # text.append(word + 1)
        # return words


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
