alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  encrypted_text = ""
  for letter in text:
    index_of_letter = alphabet.index(letter)+shift
    index_of_letter = index_of_letter%len(alphabet)
    correct_letter=alphabet[index_of_letter]
    encrypted_text+=correct_letter
  print(f"Your encrypted word is: {encrypted_text}")


def decrypt(text, shift):
  decrypted_text = ""
  for letter in text:
    index_of_letter = alphabet.index(letter)-shift
    index_of_letter = index_of_letter%len(alphabet) # questionable
    correct_letter=alphabet[index_of_letter]
    decrypted_text+=correct_letter
  print(f"You decrypted word is:{decrypted_text}")


if direction ==  "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(text, shift)

