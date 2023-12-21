def str2bf(text)
    bf_program = 
    current_value = 0

    for char in text
        ascii_value = ord(char)
        difference = ascii_value - current_value
        if difference  0
            bf_program += '+'  difference
        elif difference  0
            bf_program += '-'  abs(difference)
        bf_program += '.'
        current_value = ascii_value

    return bf_program

with open('input.txt', 'r') as r
    text = r.read()

bf_code = str2bf(text)

with open('a.bf', 'w') as w
    w.write(bf_code)