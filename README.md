# Ming's Mosaic

> [!NOTE]  
> This encryption and decryption method is an ongoing project to explore cryptography and increase security. The currently provided latest version is **Ming's Mosaic v2.2**.
> 
> **Disclaimer:** This tool was created for educational and recreational purposes. Do not use this code for malicious activities. The author is not responsible for any misuse.
> 
> **License:** This code is entirely open-source. Anyone is free to use, edit, and share the code—no credit required!

## 📖 General Information

I named my first-ever cipher-decipher tool **"Ming's Mosaic"**. While it might not beat RSA encryption, it's a fun, robust project born out of curiosity! 

In essence, it's a layered encryption tool that scrambles and unscrambles messages using a custom blend of data obfuscation and classic ciphers.

**Future Considerations for Keys:** Currently, users input the shifts and keys manually via the terminal. I previously considered having users append numbers/text at the start or end of the ciphertext to indicate the keys and sender, but that is both a hassle and a security vulnerability. Future versions will focus on making key handling much more robust and automated.

---

## 🚀 Version History

- [x] **Ming's Mosaic v1:** Base logic implementation (Standard Caesar Cipher).
- [x] **Ming's Mosaic v2.1:** Added a Vigenère cipher layer.
- [x] **Ming's Mosaic v2.2:** Added a secondary Caesar cipher after the Vigenère layer for compounded scrambling.
- [ ] **Ming's Mosaic v3:** Implement a custom cipher *before* the ASCII encoding step.
- [ ] **Ming's Mosaic v4:** *TBD*

---

## How It Works

Ming's Mosaic passes your text through a strict pipeline of conversions and ciphers. Here is the exact data flow for **v2.2**:

### Encrypting (Scrambling)

1. **Custom ASCII Encoding (`ltoc`)**
   * **Split & Convert:** Splits the plaintext into individual letters and converts each to its denary ASCII equivalent (e.g., `"A"` = `65`).
   * **Hex Manipulation:** Takes the individual digits (e.g., `6` and `5`), treats them as characters, and finds their hex equivalents (e.g., `'6'` = `36`).
   * **Swap:** Swaps the hex-code digits around (e.g., `36` becomes `63`).
   * **Concatenate:** Combines the swapped hex-codes for the character (e.g., `"A"` becomes `6353`).
   * **Letter Mapping:** Maps the resulting numbers (0-9) to letters (A-J). For example, `6353` becomes `GDFD`.

2. **Caesar Cipher #1**
   * The A-J character string is shifted using a standard Caesar cipher based on a user-defined numeric `shift`.

3. **Vigenère Cipher**
   * The output from the Caesar cipher is scrambled further using a Vigenère cipher, driven by a user-provided `keyword`.

4. **Caesar Cipher #2 (Final Layer)**
   * One last Caesar cipher is applied to the data. To increase security, this shift is calculated as `(user_shift + length_of_keyword)`.

---

### Decrypting (Unscrambling)

To decrypt, the program runs the encryption pipeline in exact reverse:

1. **Reverse Caesar Cipher #2**
   * Undoes the final layer using a reverse shift of `-(user_shift + length_of_keyword)`.

2. **Reverse Vigenère Cipher**
   * Reverses the Vigenère shift using the exact same `keyword` provided during encryption.

3. **Reverse Caesar Cipher #1**
   * Undoes the foundational Caesar shift using the original user-defined `shift`.

4. **Custom ASCII Decoding (`ctol`)**
   * **Digit Mapping:** Translates the A-J letters back into their 0-9 numeric equivalents (e.g., `GDFD` becomes `6353`).
   * **Chunking & Swapping:** Breaks the numbers into pairs (e.g., `63` and `53`) and swaps them back to their original hex forms (e.g., `36` and `35`).
   * **Hex to Denary:** Converts the hex values back into their original ASCII digits (e.g., `36` = `6`, `35` = `5`).
   * **Reassembly:** Joins the digits to form the original decimal ASCII value (`65`) and translates it back to the readable character (`"A"`). All letters are mashed together into the final output.
