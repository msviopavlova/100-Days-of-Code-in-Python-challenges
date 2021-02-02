
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount = shift_amount * -1
  for letter in start_text:
    if letter in alphabet:
      index_of_letter = alphabet.index(letter)+shift_amount
      index_of_letter = index_of_letter%len(alphabet)
      correct_letter=alphabet[index_of_letter]
      end_text += correct_letter
    else:
      end_text += letter
  print(f"Ths is your {cipher_direction}d message: {end_text}")



should_continue = True
while should_continue:
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)
  result = input("Type 'yes' if you would like to continue, 'no' if not \n")
  if result == "no":
    should_continue = False
    print("Goodbye")


#OLD SOLUTION

# def encrypt(text, shift):
#   encrypted_text = ""
#   for letter in text:
#     index_of_letter = alphabet.index(letter)+shift
#     index_of_letter = index_of_letter%len(alphabet)
#     correct_letter=alphabet[index_of_letter]
#     encrypted_text+=correct_letter
#   print(f"Your encrypted word is: {encrypted_text}")
#
#
# def decrypt(text, shift):
#   decrypted_text = ""
#   for letter in text:
#     index_of_letter = alphabet.index(letter)-shift
#     index_of_letter = index_of_letter%len(alphabet) # questionable
#     correct_letter=alphabet[index_of_letter]
#     decrypted_text+=correct_letter
#   print(f"You decrypted word is:{decrypted_text}")

#
# if direction ==  "encode":
#   encrypt(text, shift)
# elif direction == "decode":
#   decrypt(text, shift)


# NEW SOLUTION




















