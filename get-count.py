def get_count(sentence):  # <-- MUST be named get_count
    vowels = "aeiou"
    count = 0
    
    # The input is guaranteed to be lowercase letters and/or spaces,
    # so we don't need to convert case or handle non-vowel letters.
    for char in sentence:
        if char in vowels:
            count += 1
            
    return count
  print(f"Liczba samogłosek w '{test_string}' to: {result}")
