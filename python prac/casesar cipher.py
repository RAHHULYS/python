alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text,shift_amount,encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabets:
            cipher_text += letter
        else:
            shifted_position = alphabets.index(letter) + shift_amount
            shifted_position %= len(alphabets)
            cipher_text += alphabets[shifted_position]
    print(f"Here is the {encode_or_decode}d Result :{cipher_text}")

should_continue = True

while should_continue:
    choice = input("Type 'encode' to encrypt or 'decode' to decrypt:").lower()
    text = input("Enter the message :").lower()
    shift = int(input("Enter the shift:"))
    caesar(text, shift, choice)
    option = input("Enter 'yes' to continue or 'no' to stop the process:").lower()
    if option == "no":
       should_continue = False
