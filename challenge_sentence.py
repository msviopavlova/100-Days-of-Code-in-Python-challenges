
def is_palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalpha():
            string+=char
    return string[::-1].casefold() == string.casefold()


my_sentence = input("Please enter a sentence here: ")

if is_palindrome_sentence(my_sentence):
    print("'{}' is a palindrome".format(my_sentence))
else:
    print("'{}' is not a palindrome".format(my_sentence))

