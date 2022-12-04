
from typing import List

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def find_common_item(compartment_1: str, compartment_2: str):
    for c in compartment_2:
        if c in compartment_1:
            return c
    return ''

def build_priority_val_map():
    val_map = {}
    for index, ch in enumerate(ALPHABET):
        val_map[ch] = index+1
    return val_map

def find_common_in_group(group):
    running_intersection = set(group[0])
    for rucksack in group:
        running_intersection = running_intersection.intersection(set(rucksack))
    
    return list(running_intersection)[0]
    

if __name__ == "__main__":
    priorities = []
    badge_priorities = []
    priority_val_map = build_priority_val_map()
    group = []
    with open('rucksack.txt', 'r') as input:
        for line in input:
            compartment_1 = line[:len(line)//2]
            compartment_2 = line[len(line)//2:]

            common_item = find_common_item(compartment_1, compartment_2)
            priorities.append(priority_val_map[common_item])

            # Challenge 2
            group.append(line.strip('\n'))
            if len(group) < 3:
                continue
            
            badge = find_common_in_group(group)
            badge_priorities.append(priority_val_map[badge])
            group = []
        print(f"The priority sum of duplicate items in the rucksacks is: {sum(priorities)}")
        print(f"The priority sum of badges for all groups of 3 elves is: {sum(badge_priorities)}")
        
