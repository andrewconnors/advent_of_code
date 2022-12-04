
def check_full_overlap(a1: str, a2: str) -> bool:
    a1_low = int(a1.split('-')[0])
    a1_high = int(a1.split('-')[1])
    a2_low = int(a2.split('-')[0])
    a2_high = int(a2.split('-')[1])

    # check first encapsulated in second and then 
    # check second encapsulated in first.
    return (a1_low >= a2_low and a1_high <= a2_high) or (a2_low >= a1_low and a2_high <= a1_high)

def check_overlap(a1: str, a2: str) -> bool:
    a1_low = int(a1.split('-')[0])
    a1_high = int(a1.split('-')[1])
    a2_low = int(a2.split('-')[0])
    a2_high = int(a2.split('-')[1])

    # check for no overlap and return opposite
    return not (a1_high < a2_low or a1_low > a2_high)
if __name__ == "__main__":
    full_overlap_count = 0
    any_overlap_count = 0
    with open('cleaning.txt', 'r') as input:
        for line in input:
            assignment_1: str = line.strip('\n').split(',')[0]
            assignment_2: str = line.strip('\n').split(',')[1]
            full_overlap: bool = check_full_overlap(assignment_1, assignment_2)
            if full_overlap:
                full_overlap_count += 1
            
            overlap: bool = check_overlap(assignment_1, assignment_2)
            if overlap:
                any_overlap_count += 1
        
        print(f"The amount of section assignments that fully overlap are: {full_overlap_count}")
        print(f"The amount of section assignments that have any overlap are: {any_overlap_count}")
