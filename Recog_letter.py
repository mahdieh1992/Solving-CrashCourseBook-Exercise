def recognize_letter(words):
    # recognize each letter of words that it's upperCase or lowerCase
    count_upper = 0
    count_lower = 0
    for letter in words:
        if letter.isupper():
            count_upper += 1
        elif letter.islower():
            count_lower += 1
        else:
            pass
    result_upper = f"count letter upper is {count_upper}"
    result_lower = f"count letter lower is {count_lower}"   
    return result_upper,result_lower


while True:
    words = input()
    if words == 'q':
        break
    else:
       result = recognize_letter(words)
       for r in result:
          print(r)  