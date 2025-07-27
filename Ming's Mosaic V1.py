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



#-----DECIPHER-----
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
#-----DECIPHER-----



#-----CIPHER-----
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
#-----CIPHER-----


print("|\/| | |\| (_, _\~   |\/| () _\~ /\ | ( \n")
print("You are now using 'Ming's Mosaic' \n")
print("-----#----#-----#-----#-----#----- \n")
    

while True:
    print("\n")
    shift = int(input("Want to share a special number?_"))
    print("-----#~~~~~#-----")
    state = input("Scramble or unscramble (s/u)?_").lower()
    print("-----#~~~~~#-----")

    # encoding
    if state in ["s", "scramble", "c", "cipher", "encode", "encrypt"]:
        plaintxt = input("Enter in your text_").upper()
        x = ltoc(plaintxt)
        y = cEnc(x, shift)
    
        print("-----#~~~~~#-----")
        print("\n")
        print("Here's your scrambled eggs!")
        print("\n")
        print(y)

    # deocoding
    elif state in ["u", "unscramble", "d", "decipher", "decode", "decrypt"]:
        ciphertxt = input("Enter in your text_").upper()
        x = cDec(ciphertxt, shift)
        y = ctol(x)
    
        print("-----#~~~~~#-----")
        print("\n")
        print("Here's your unscrambled eggs!")
        print("\n")
        print(y)
        print("\n")
