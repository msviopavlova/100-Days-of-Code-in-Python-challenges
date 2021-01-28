#this is the first lesson about functions from Udemy Python Course

# def multiply(x, y): #parameters
#     result = x * y
#     return result

def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


word = input("Please enter a word: ")

if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))


# answer = multiply(10.5, 4) #argumments to be passed
# print(answer)
#
# forty_two = multiply(6, 7)
# print(forty_two)
#
# print("**************************************")
#
#
# for val in range(1, 5): #not including 5 = 1 2 3 4
#     two_times = multiply(2, val) # val will be an iterator in the range from 1 to 5 (1 2 3 4)each time around , val will be y in multiply()
#     print(two_times)




