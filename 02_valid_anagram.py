# Anagrams are set are words that has the same characters of alphatbets in them 
# e.g  S: CAT and T: TAC 
# S and T are anagrams of each other 
# Confirm if the length of the words are same, if they are not then are not anagrams of each other 
# Make a 26 character  frequency array or list by default or the frequencies are going to be 0
# Loop over the characters of the first word, for every character get the index of the characters in the alphatbets and increment the frequency position of that index by one
# Do same loop for the characters in the second word, but this time decrement the frequency by -1
# At the end if they are anagrams, the freq across the table is going to be 0


def check_anagrams(s,t):
    character_freq_table = [0] * 26 # This returns an array of 26 characters and we assume that their freq is  0

    if len(s) != len(t):
        return False

    for char in s:
        char_index_in_alphabets = ord(char) - ord('a')
        character_freq_table[char_index_in_alphabets] +=1

    for char in t:
            char_index_in_alphabets = ord(char) - ord('a')
            character_freq_table[char_index_in_alphabets] -=1

    print(character_freq_table)
    for items in character_freq_table:
         if items != 0:
            return False
    




check_anagrams("silent", "listey")