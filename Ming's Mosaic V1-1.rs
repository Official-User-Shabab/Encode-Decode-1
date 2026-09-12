// trying to convert this to Rust for practice

use std::io::{self, Write};

// -----CAESAR PART -----

fn c_enc(text: &str, shift: i32) -> String {
  
    let mut result = String::new();

    for c in text.chars() {
        if c.is_ascii_uppercase() {
          
            let number = c as i32 - 'A' as i32;
          
            let shifted = (number + shift) % 26;
            let new_char = (shifted + 'A' as i32) as u8 as char;

            result.push(new_char);
          
        } else {
          
            result.push(c);
          
        }
    }

    result
}


fn c_dec(text: &str, shift: i32) -> String {
    c_enc(text, -shift)
}

// -----CIPHER-----

fn ltoc(text: &str) -> String {
  
    let digit_to_letter: Vec<char> = "ABCDEFGHIJ".chars().collect();
  
    let mut result = String::new();
    
    // Convert to uppercase and remove spaces
  
    let cleaned_text = text.to_uppercase().replace(" ", "");
    
    for c in cleaned_text.chars() {
        if !c.is_ascii_uppercase() { continue; }
        
        let ascii_val = c as u8;
        let ascii_str = ascii_val.to_string();
        
        for digit_char in ascii_str.chars() {
            let digit = digit_char.to_digit(10).unwrap();
            let hex_val = format!("3{:x}", digit); // convert to hex string prepended with "3"
            
            // Swap characters by reversing
            let swapped: String = hex_val.chars().rev().collect();
            
            // Map to A-J
            for d_char in swapped.chars() {
                let d = d_char.to_digit(10).unwrap() as usize;
                result.push(digit_to_letter[d]);
            }
        }
    }
    result
}


// -----DECIPHER-----


fn ctol(code: &str) -> String {
  
    let mut output = String::new();
    let code_chars: Vec<char> = code.chars().collect();
    
    for chunk in code_chars.chunks(4) {
      
        if chunk.len() < 4 { continue; }
        
        let mut digits = Vec::new();
      
        for pair in chunk.chunks(2) {
          
            if pair.len() < 2 { continue; }
            
            let c2 = pair[0]; // original second char (the hex digit)
            
            // Convert letter back to digit ('A -> 0, 'B' -> 1)
            let d2 = c2 as u8 - b'A'; 
            digits.push(d2.to_string());
          
        }

      
        if digits.len() == 2 {
            let ascii_str = digits.join("");
            if let Ok(ascii_code) = ascii_str.parse::<u8>() {
                output.push(ascii_code as char);
            }
          
        }
      
    }
    output
}


fn main() {
    println!("|\\/| | |\\| (_, _\\~   |\\/| () _\\~ /\\ | ( \n");
    println!("You are now using 'Ming's Mosaic' \n");
    println!("-----#----#-----#-----#-----#----- \n");

    loop {
        println!("\n");
        
        let mut input = String::new();
        print!("Want to share a special number?_");
        io::stdout().flush().unwrap();
        io::stdin().read_line(&mut input).unwrap();
        
        // Rust's safety: handling the case where  user types a letter instead of a number
      
        let shift: i32 = match input.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Please enter a valid number.");
                continue;
            }
        };
        
        println!("-----#~~~~~#-----");
        print!("Scramble or unscramble (s/u)?_");
        io::stdout().flush().unwrap();
        
        let mut state = String::new();
        io::stdin().read_line(&mut state).unwrap();
        let state = state.trim().to_lowercase();
        
        println!("-----#~~~~~#-----");
        
        if ["s", "scramble", "c", "cipher", "encode", "encrypt"].contains(&state.as_str()) {
            print!("Enter in your text_");
            io::stdout().flush().unwrap();
            let mut plaintxt = String::new();
            io::stdin().read_line(&mut plaintxt).unwrap();
            
            let x = ltoc(&plaintxt.trim());
            let y = c_enc(&x, shift);
            
            println!("-----#~~~~~#-----");
            println!("\nHere's your scrambled eggs!\n\n{}", y);
            
        } else if ["u", "unscramble", "d", "decipher", "decode", "decrypt"].contains(&state.as_str()) {
            print!("Enter in your text_");
            io::stdout().flush().unwrap();
            let mut ciphertxt = String::new();
            io::stdin().read_line(&mut ciphertxt).unwrap();
            
            let x = c_dec(&ciphertxt.trim(), shift);
            let y = ctol(&x);
            
            println!("-----#~~~~~#-----");
            println!("\nHere's your unscrambled eggs! \n\n{}", y);
        } else {
            
            println!("Invalid command.");
        }
    }
  
}
