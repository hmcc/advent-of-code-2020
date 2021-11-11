def read_input(filename):
    program = []
    with open(filename) as file:
        for line in file:
            instruction = parse_line(line)
            if instruction:
                program.append(instruction)
    return program


def parse_line(line):
    instruction = line.strip().split()
    instruction[1] = int(instruction[1])
    return instruction


def execute_instruction(program, pointer, acc):
    instruction = program[pointer]
    if (instruction[0] == 'acc'):
        acc = acc + instruction[1]
        pointer = pointer + 1
    elif(instruction[0] == 'jmp'):
        pointer = pointer + instruction[1]
    elif(instruction[0] == 'nop'):
        pointer = pointer + 1
    else:
        print(f'invalid instruction at {pointer}: {instruction}')
        pointer = pointer + 1
    return (pointer, acc)
    

def print_error(program, pointer, acc):
    print(f'duplicate instruction found at {pointer} {program[pointer][:2]} visited at {program[pointer][2:]}')
    print(f'accumulator is {acc}')


def swap(instruction):
    if (instruction[0] == 'jmp'):
        instruction[0] = 'nop'
    elif(instruction[0] == 'nop' and instruction[1] != 0):
        instruction[0] = 'jmp'
    else:
        print(f'invalid instruction for swap {instruction}')


def reset(program):
    return [i[:2] for i in program]


def run_all_programs(program):
    for i in (i for i in program if i[0] in ('nop', 'jmp') and i != ['nop', 0]):
        swap(i)
        ran_to_completion, acc = execute(program)
        if ran_to_completion:
            print('completed successfully!')
            print(f'accumulator is {acc}')
            return acc
        swap(i)
    return 0


def execute(program):
    pointer = acc = 0
    counter = 1
    program = reset(program)
    while (pointer < len(program)):
        program[pointer].append(counter)
        if (len(program[pointer]) > 3):
            print_error(program, pointer, acc)
            break
        pointer, acc = execute_instruction(program, pointer, acc)
        counter = counter + 1
    return (pointer >= len(program), acc)


input_program = read_input('day8/input')
# ran_to_completion = execute(input_program)
run_all_programs(input_program)
