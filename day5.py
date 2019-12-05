def init_memory():
    return list(map(int, "".split(','))) # input goes here, per usual

def split_opcode(opcode):
    digits = [0, 0, 0, 0, 0]
    opcode_digits = list(reversed([int(digit) for digit in list(str(opcode))]))
    for i in range(len(opcode_digits)):
      digits[i] = opcode_digits[i]
    return list(reversed(digits))

def run_program(program, program_input):
    idx = 0
    while idx < len(program):
        opcode_obj = split_opcode(program[idx])
        opcode = opcode_obj[4]
        par1_mode = opcode_obj[2]
        par2_mode = opcode_obj[1]
        if opcode == 1:
            if par1_mode == 0:
                par1 = program[program[idx + 1]]
            else:
                par1 = program[idx + 1]
            if par2_mode == 0:
                par2 = program[program[idx + 2]]
            else:
                par2 = program[idx + 2]
            dest = program[idx + 3]
            program[dest] = par1 + par2
            idx += 4
        elif opcode == 2:
            if par1_mode == 0:
                par1 = program[program[idx + 1]]
            else:
                par1 = program[idx + 1]
            if par2_mode == 0:
                par2 = program[program[idx + 2]]
            else:
                par2 = program[idx + 2]
            dest = program[idx + 3]
            program[dest] = par1 * par2
            idx += 4
        elif opcode == 3:
            program[program[idx + 1]] = program_input
            idx += 2
        elif opcode == 4:
            print(program[program[idx + 1]])
            idx += 2
        elif opcode == 5:
            if par1_mode == 0:
                par1 = program[program[idx + 1]]
            else:
                par1 = program[idx + 1]
            if par2_mode == 0:
                par2 = program[program[idx + 2]]
            else:
                par2 = program[idx + 2]
            if par1 != 0:
                idx = par2
            else:
                idx += 3
        elif opcode == 6:
            if par1_mode == 0:
                par1 = program[program[idx + 1]]
            else:
                par1 = program[idx + 1]
            if par2_mode == 0:
                par2 = program[program[idx + 2]]
            else:
                par2 = program[idx + 2]
            if par1 == 0:
                idx = par2
            else:
                idx += 3
        elif opcode == 7:
            if par1_mode == 0:
                par1 = program[program[idx + 1]]
            else:
                par1 = program[idx + 1]
            if par2_mode == 0:
                par2 = program[program[idx + 2]]
            else:
                par2 = program[idx + 2]
            if par1 < par2:
                program[program[idx + 3]] = 1
            else:
                program[program[idx + 3]] = 0
            idx += 4
        elif opcode == 8:
            if par1_mode == 0:
                par1 = program[program[idx + 1]]
            else:
                par1 = program[idx + 1]
            if par2_mode == 0:
                par2 = program[program[idx + 2]]
            else:
                par2 = program[idx + 2]
            if par1 == par2:
                program[program[idx + 3]] = 1
            else:
                program[program[idx + 3]] = 0
            idx += 4
        elif opcode == 9:
            break

run_program(init_memory(), 1)
run_program(init_memory(), 5)
