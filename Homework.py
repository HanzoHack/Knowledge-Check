# Even or odd
def even_or_odd(number):
    return "Even" if number %2 == 0 else "Odd"

# Convert a number into a string
def number_to_string(num):
    return str(num)

# Vowel Count
def get_count(sentence):
    num_vowels = 0
    vowels = 'aeiou'
    for x in sentence:
        if x in vowels:
            num_vowels += 1
    return num_vowels