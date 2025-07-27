# Encode-Decode-1

I've named my first ever cipher-decipher as "Ming's Mosaic". It won't beat RSA, but it's something...

In essence, it's a layered encryption tool that scrambles and unscrambles messages using a custom blend of classic ciphers.

## How it works

### Encrypting

#### Encryption (Scrambling)

1. **Letter-to-Character Conversion**:
   Each letter in the input is converted to a unique sequence using its ASCII code and a custom A–J digit-letter mapping.
2. **Caesar Cipher #1**:
   The resulting characters are encrypted using a Caesar cipher with a user-defined shift value.
3. **Vigenère Cipher**:
   The output is further encrypted using a Vigenère cipher with a user-provided keyword.
4. **Caesar Cipher #2 (Final Layer)**:
   One last Caesar cipher is applied using a shift of `(user_shift + length_of_key)` to enhance security.

#### ASCII Encoding

1) Splits all letters individually
2) Converts each letter into its ASCII equivalent for denary (eg "A" = 65)
3) Converts each of the individual numbers into its hex-code from ASCII (eg '6' = 36)
4) Swaps the hex-codes around (eg 36 becomes 63)
5) Hence puts the hex-codes for the word together (eg "A" = 6353)
6) Matches each individual number from 0-9 with A-J

---

### Decrypting

#### Decryption (Unscrambling)

1. **Caesar Cipher #2 (Reverse)**:
   The final Caesar layer is undone using the same `(shift + key_length)` value.
2. **Vigenère Decryption**:
   The Vigenère cipher is reversed using the same keyword.
3. **Caesar Cipher #1 (Reverse)**:
   The original Caesar cipher is reversed using the user's shift.
4. **Character-to-Letter Conversion**:
   The encoded characters are converted back to readable letters using the inverse A–J digit-letter mapping.

#### ASCII Decoding

1) Matches each individual letter from A-J with 0-9
2) Hence finds the nibbled-hex-codes for the word together (eg 6353)
3) Swaps the coupled hex-codes around (eg 63 becomes 36)
4) Converts each of the hex-code into its denary equivalent from ASCII (eg 36 = 6)
5) Converts each decimal number into its ASCII equivalent for denary (eg 65 = "A")
6) Mashes all leters together and outputs it (hence the output is also just one massive word)

## Version History

- [x] ```Ming's Mosaic v1``` (Basically just a caesar cipher)
- [x] ```Ming's Mosaic v2.1``` (Applied vigenere cipher)
- [x] ```Ming's Mosaic v2.2``` (Aded a caesar cipher after vigenere)
- [ ] ```Ming's Mosaic v3``` (A cipher added before ASCII encoding)
