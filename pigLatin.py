#Oscar Levin

#English to Pig Latin Translate

word = input("Enter a word: ")

words = word

vowels = ["a", "e", "i", "o", "u"]

if (word[0] in vowels):

    word = word + "yay"
    
else:

    word = word[1:] + word[:1] + "ay"
    
print("Pig Latin word of '%s' is '%s.'" % (words, word))
