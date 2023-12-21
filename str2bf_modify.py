def str2bf(text):
    def closest_distance(target, memory):
        closest = None
        for idx, value in enumerate(memory):
            if closest is None or abs(target - value) < abs(target - memory[closest]):
                closest = idx
        return closest, target - memory[closest]

    memory = [0]
    bf_program = ""
    current_cell = 0

    for char in text:
        ascii_value = ord(char)
        closest_cell, distance = closest_distance(ascii_value, memory)

        bf_program += '>' * (closest_cell - current_cell) if closest_cell > current_cell else '<' * (current_cell - closest_cell)
        current_cell = closest_cell

        bf_program += '+' * distance if distance > 0 else '-' * abs(distance)

        bf_program += '.'

        memory[current_cell] = ascii_value

        if current_cell == len(memory) - 1:
            memory.append(0)

    return bf_program

with open('input.txt', 'r') as r:
    text = r.read()

bf_code = str2bf(text)

with open('b.bf', 'w') as w:
    w.write(bf_code)