string_with_words = input("Please enter the list of words (separated by whitespace): ")

list_of_words = string_with_words.split()
print("Original list:", list_of_words)

short_word = list_of_words[0]
long_word = list_of_words[0]
short_word_index = 0
long_word_index = 0

for i in range(0, len(list_of_words)):
    if len(list_of_words[i]) < len(short_word):
        short_word = list_of_words[i]
        short_word_index = i
    if len(list_of_words[i]) > len(long_word):
        long_word = list_of_words[i]
        long_word_index = i

if short_word_index != long_word_index:
    print("The shortest word is:", short_word)
    print("The longest word is:", long_word)
    temp = short_word
    list_of_words[short_word_index] = long_word
    list_of_words[long_word_index] = temp
    print("The new list is:", list_of_words)
else:
    print("All the words in the list have the same length, no changes were done")