
def split_input(line: str):
    assignments = line.strip('\n').split(',')
    a1_low = int(assignments[0].split('-')[0])
    a1_high = int(assignments[0].split('-')[1])
    a2_low = int(assignments[1].split('-')[0])
    a2_high = int(assignments[1].split('-')[1])

    return (a1_low, a1_high, a2_low, a2_high)

def check_full_overlap(a1_low: int, a1_high: int, a2_low: int, a2_high: int) -> bool:
    # check first encapsulated in second and then 
    # check second encapsulated in first.
    return (a1_low >= a2_low and a1_high <= a2_high) or (a2_low >= a1_low and a2_high <= a1_high)

def check_overlap(a1_low: int, a1_high: int, a2_low: int, a2_high: int) -> bool:
    # check for no overlap and return opposite
    return not (a1_high < a2_low or a1_low > a2_high)

if __name__ == "__main__":
    full_overlap_count = 0
    any_overlap_count = 0
    with open('cleaning.txt', 'r') as input:
        for line in input:
            a1_low, a1_high, a2_low, a2_high = split_input(line)
            full_overlap_count += 1 if check_full_overlap(a1_low, a1_high, a2_low, a2_high) else 0
            any_overlap_count += 1 if check_overlap(a1_low, a1_high, a2_low, a2_high) else 0
        
        print(f"The amount of section assignments that fully overlap are: {full_overlap_count}")
        print(f"The amount of section assignments that have any overlap are: {any_overlap_count}")
