#! /usr/bin/env python3
from random import SystemRandom

_sysrand: SystemRandom = SystemRandom()

def rand_below(exclusive_upper_bound):
    """
    Return a random int in the range [0, n).
    This function was cribbed from the `secrets` library in order to eliminate its 
    dependency on OpenSSL for features not used in `randomstr`.
    """
    if exclusive_upper_bound <= 0:
        raise ValueError("Upper bound must be positive.")
    
    # The use of __ is inherited from the `secrets` library, an 
    # implmentation that is considered secure for cryptographic use by 
    # the Python community.
    return _sysrand._randbelow(exclusive_upper_bound) # pyrefly: ignore

def str_to_unique_char_list(string):
    """
    Takes an array and converts it into a string of unique characters.
    """
    return ''.join(set(string))  # Casting string to set de-dupes the characters.


def gen_random_str(rand_str_len, disallow_list):
    """
    Generates the ramdom string.
    """
    output = ''
    i = 0
    while i < rand_str_len:
        ascii_val = rand_below(94) + 33

        # This should never happen, but if it does, fail noticably.
        if ascii_val > 126 or ascii_val < 33:
            raise Exception('Generated ASCII value out of range of acceptable characters.')
            exit(1)

        newchar = chr(ascii_val)
        if not newchar in disallow_list:
            output = output + newchar
            i += 1
    return output


def gen_random_diverse_str(rand_str_len, disallow_list, no_special = False, no_upper = False, no_lower = False, no_numeric = False):
    """
    By default, generates a ramdom string that has a lower case letter, an upper case letter, a number, and a non alpha-numeric character.
    """
    output = ''

    if not no_special:
        output += gen_special_single_chr()   
    if not no_upper:
        output += gen_upper_single_chr()
    if not no_lower:
        output += gen_lower_single_chr()
    if not no_numeric:
        output += gen_numeric_single_chr()

    output = shuffle_string(output)

    i = 0
    rand_str_len = rand_str_len - len(output)
    while i < rand_str_len:
        ascii_val = rand_below(94) + 33

        # This should never happen, but if it does, fail noticably.
        if ascii_val > 126 or ascii_val < 33:
            raise Exception('Generated ASCII value out of range of acceptable characters.')
            exit(1)

        newchar = chr(ascii_val)
        if not newchar in disallow_list:
            output = output + newchar
            i += 1

            if ascii_val >= 65 and ascii_val <= 90:
                has_upper = True
            elif ascii_val >= 97 and ascii_val <= 122:
                has_lower = True
            elif ascii_val >= 48 and ascii_val <= 57:
                has_number = True
            else:
                has_special = True

        output = shuffle_string(output)
    # end while
    return output


def shuffle_string(target_string):
    """
    Returns a string with the contents of target_string in a random order.
    """
    target_list = list(target_string)
    result = ""
    target_list_len = len(target_list)
    while target_list_len > 0:
        random_index = rand_below(target_list_len)
        result = result + target_list[random_index]
        target_list.pop(random_index)
        target_list_len = len(target_list)
    
    return result


def gen_chr_sequence_str (first, last, separator=''):
    """
    Generates an ordered string of ASCII characters. first and last are inclusive.
    """
    return separator.join([chr(i) for i in range(first, (last + 1))])


def gen_special_chr_str ():
    """
    Generates a string of all special characters (non-whitespace, non-alphanumeric) in the lower ASCII range.
    """
    if 'special_sequence' not in  gen_special_chr_str.__dict__:
        special_sequence = gen_chr_sequence_str(33, 47) + gen_chr_sequence_str(58, 64) + gen_chr_sequence_str(91, 96) +gen_chr_sequence_str(123, 126)
    return special_sequence


def gen_numeric_chr_str ():
    """
    Generates a string of all numeric characters.
    """
    if 'num_sequence' not in gen_numeric_chr_str.__dict__:
        num_sequence = gen_chr_sequence_str(48, 57)
    return num_sequence


def gen_lower_chr_str ():
    """
    Generates a string of all lower case letters.
    """
    if 'lower_sequence' not in gen_lower_chr_str.__dict__:
        lower_sequence = gen_chr_sequence_str(97, 122)
    return lower_sequence


def gen_upper_chr_str ():
    """
    Generates a string of all upper case letters.
    """
    if 'upper_sequence' not in gen_upper_chr_str.__dict__:
        upper_sequence = gen_chr_sequence_str(65, 90)
    return upper_sequence


def gen_special_single_chr():
    """Generates a single special character as a string.
    Return: A string containing a single special character.
    """
    special_sequence = gen_special_chr_str()
    return special_sequence[rand_below(len(special_sequence))]


def gen_numeric_single_chr():
    """Generates a single numeric character as a string.
    Return: A string containing a single numeric character.
    """
    numeric_sequence = gen_numeric_chr_str()
    return numeric_sequence[rand_below(len(numeric_sequence))]


def gen_lower_single_chr():
    """Generates a single lower character as a string.
    Return: A string containing a single lower character.
    """
    lower_sequence = gen_lower_chr_str()
    return lower_sequence[rand_below(len(lower_sequence))]


def gen_upper_single_chr():
    """Generates a single upper character as a string.
    Return: A string containing a single upper character.
    """
    upper_sequence = gen_upper_chr_str()
    return upper_sequence[rand_below(len(upper_sequence))]
