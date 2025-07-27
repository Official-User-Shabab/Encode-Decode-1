#-----VIGENERE PART-----
def generate_key(text, key):
    key = list(key)
    if len(key) == len(text):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(plaintext, key):
    key = generate_key(plaintext, key)
    ciphertext = ""
    for p, k in zip(plaintext, key):
        if p.isalpha():
            shift = ord('A') if p.isupper() else ord('a')
            k_shift = ord(k.upper()) - ord('A')
            encrypted_char = chr((ord(p) - shift + k_shift) % 26 + shift)
            ciphertext += encrypted_char
        else:
            ciphertext += p  # leaves non-alphabetic characters unchanged
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    key = generate_key(ciphertext, key)
    decrypted_text = ""
    for c, k in zip(ciphertext, key):
        if c.isalpha():
            shift = ord('A') if c.isupper() else ord('a')
            k_shift = ord(k.upper()) - ord('A')
            decrypted_char = chr((ord(c) - shift - k_shift + 26) % 26 + shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += c  # leaves non-alphabetic characters unchanged
    return decrypted_text
#-----VIGENERE PART-----

#----------------------------------------------------------------------


# A=0, B=1, ..., J=9

#-----CAESAR PART-----
def cEnc(text, shift):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
            result += chr(shifted)
        else:
            result += char  # Keep other chars as is
    return result

def cDec(text, shift):
    return cEnc(text, -shift)
#-----CAESAR PART-----



#-----CHARACTER TO LETTER-----
def ctol(code):
    letter_to_digit = {ch: str(i) for i, ch in enumerate("ABCDEFGHIJ")}
    output = ""

    # Process "nibbles"
    for i in range(0, len(code), 4):
        chunk = code[i:i+4]
        digits = []
        for j in range(0, 4, 2):
            pair = chunk[j:j+2]
            if len(pair) < 2:
                continue  # safety check
            # swaps back to OG order
            swapped = pair[::-1]
            #letters to digits
            d1 = letter_to_digit.get(swapped[0])
            d2 = letter_to_digit.get(swapped[1])
            if d1 is None or d2 is None:
                continue
            digits.append(d2)  # we only care about the second digit of "3x" which was originally x

        if len(digits) == 2:
            ascii_code = int("".join(digits))
            output += chr(ascii_code)

    return output
#----------



#-----LETTER TO CHARACTER-----
def ltoc(text):
    digit_to_letter = "ABCDEFGHIJ" 

    result = ""
    for char in text.upper().replace(" ", ""):
        ascii_val = ord(char)
        if not ('A' <= char <= 'Z'):
            continue  # Skip non-letters

        for digit in str(ascii_val):
            hex_val = hex(int(digit))[2:]  # convert digit to hex (as string)
            hex_val = "3" + hex_val
            swapped = hex_val[::-1]  # swap the two characters
            for d in swapped:
                result += digit_to_letter[int(d)]

    return result
#----------


#----STARTS HERE-----

print("\n")
print("|\/| | |\| (_, _\~   |\/| () _\~ /\ | ( \n")
print("You are now using 'Ming's Mosaic' \n")
print("-----#----#-----#-----#-----#----- \n")
    

while True:
    
    print("New session started!\n")
    shift = int(input("Want to share a special number?_"))
    key = input("\nAny kind words?_").upper()
    print("-----#~~~~~#-----")
    state = input("Scramble or unscramble (s/u)?_").lower()
    print("-----#~~~~~#-----")

        # encoding
    if state in ["s", "scramble", "c", "cipher", "encode", "encrypt"]:
        plaintxt = input("Enter in your text_").upper()
        x = ltoc(plaintxt)
        y = cEnc(x, shift)
        z = vigenere_encrypt(y, key)
        final = cEnc(z, shift + len(key))  # final Caesar with x + n

        print("-----#~~~~~#-----")
        print("\n")
        print("Here's your scrambled eggs!")
        print("\n")
        print(final)
        print("\n")


        # deocoding
    elif state in ["u", "unscramble", "d", "decipher", "decode", "decrypt"]:
        ciphertxt = input("Enter in your text_").upper()
        z = cDec(ciphertxt, shift + len(key))  # reverse final Caesar
        x = vigenere_decrypt(z, key)
        y = cDec(x, shift)
        final = ctol(y)

        print("-----#~~~~~#-----")
        print("\n")
        print("Here's your unscrambled eggs!")
        print("\n")
        print(final)
        print("\n")
