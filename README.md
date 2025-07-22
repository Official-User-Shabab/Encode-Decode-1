# Encode-Decode-1

I've named my first ever cipher-decipher as "Ming's Mosaic". It won't beat RSA, but it's something...

## How it works

### Encoding

1) Takes your inputted text (the shift is the caeser cipher number)
2) Splits all letters individually
3) Converts each letter into its ASCII equivalent for denary (eg "A" = 65)
4) Converts each of the individual numbers into its hex-code from ASCII (eg '6' = 36)
5) Swaps the hex-codes around (eg 36 becomes 63)
6) Hence puts the hex-codes for the word together (eg "A" = 6353)
7) Matches each individual number from 0-9 with A-J
8) Puts it through a caesar cipher with some shift (coz its fun)
9) Outputs this new text out (all words mashed as one)

### Decoding

1) Takes your inputted text (the shift is the caeser decipher number)
2) Puts it through a caesar DE-cipher
3) Matches each individual letter from A-J with 0-9
4) Hence finds the nibbled-hex-codes for the word together (eg 6353)
5) Swaps the coupled hex-codes around (eg 63 becomes 36)
6) Converts each of the hex-code into its denary equivalent from ASCII (eg 36 = 6)
8) Converts each decimal number into its ASCII equivalent for denary (eg 65 = "A")
9) Mashes all leters together and outputs it (hence the output is also just one massive word)
