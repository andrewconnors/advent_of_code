from typing import Dict, List, Tuple

STACK_ITEM_LENGTH = 4

def process_stack_input(input: str) -> Dict[int, List]:
    result: Dict[int, List] = {}
    input_list = input.split('\n')

    # Load up result with keys
    for c in input_list[-1]:
        if c.isdigit():
            result[int(c)] = []
    input_list.pop()

    # process stack levels from bottom to top
    for row in input_list[::-1]:
        char_index = 0
        col_index = 1
        while char_index < len(row):
            if row[char_index] == '[':
                result[col_index].append(row[char_index + 1])

            char_index += STACK_ITEM_LENGTH
            col_index = col_index + 1 if col_index != len(result) else 1

    return result

def parse_instruction(instruction: str) -> Tuple[int, int, int]:
    parsed = []
    for word in instruction.strip('\n').split(' '):
        if word.isdigit():
            parsed.append(int(word))
    
    return (parsed[0], parsed[1], parsed[2])
        

if __name__ == "__main__":
    stack_map: Dict[int, List] = {}
    stack_input = ''
    with open('crate_stacking.txt', 'r') as input:
        # Load stack into input string
        for line in input:
            if not stack_map:
                if line == '\n':
                    stack_map = process_stack_input(stack_input[:-1])
                else:
                    stack_input += line
            else:
                amount, from_stack, to_stack = parse_instruction(line)

                # Solution 1
                # for _ in range(amount):
                    # stack_map[to_stack].append(stack_map[from_stack].pop())

                # Solution 2
                stack_map[to_stack].extend(stack_map[from_stack][-amount:])
                stack_map[from_stack] = stack_map[from_stack][:-amount]
                    
    
    print(f"top items in each stack are: {''.join([stack_map[x][-1] for x in stack_map.keys()])}")

        
        

