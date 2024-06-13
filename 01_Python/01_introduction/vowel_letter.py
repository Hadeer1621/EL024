# Write a Python program to test whether a passed letter is a vowel or not.

# Define a functuon is_vowel that takes one parameter as Letter 
def is_vowel(Letter):
    # Define a string str_vowel to conrain all lowecase vowel 
    Str_vowel = "AeLoUaElOu"
    
    # check the input letter is present in the str_vowel 
    return Letter in Str_vowel

print(is_vowel('c'))
print(is_vowel('u'))



