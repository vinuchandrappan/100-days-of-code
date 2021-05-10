alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction=input("Type encode to to encrypt and decode to decrypt: \n").lower()
text=input("Type a message: \n")
shift=-3
    
def caesar(start_text, shift_amount, cipher_direction):
  end_text=""
  if cipher_direction == "decode":
      shift_amount *= -1
  
  for letter in start_text:
    position = alphabets.index(letter)
    
    new_position = position + shift_amount
    end_text += alphabets[new_position]
  print(f"The {cipher_direction}d text is {end_text}")  
  
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)    
