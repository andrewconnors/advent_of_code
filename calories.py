from typing import List

from dataclasses import dataclass

@dataclass
class Elf:
    identifier: int = 0
    calorie_load: int = 0

if __name__ == "__main__":
    calorie_totals_by_elf: List[Elf] = []
    current_elf: Elf = Elf()

    with open("calories.txt", "r") as input:
        for line in input:
            if line == "\n":
                calorie_totals_by_elf.append(current_elf)
                current_elf = Elf(len(calorie_totals_by_elf)+1, 0)
            else:
                current_elf.calorie_load += int(line)

    # Get top calorie carrying elves
    calorie_totals_by_elf.sort(key=lambda elf: elf.calorie_load, reverse=True)
    print(
        f"The elf carrying the most calories is elf {calorie_totals_by_elf[0].identifier} with {calorie_totals_by_elf[0].calorie_load} calories\n"
    )
    print(f"The 3 elves carrying the most calories are elves {calorie_totals_by_elf[0].identifier}, {calorie_totals_by_elf[1].identifier}, and {calorie_totals_by_elf[2].identifier}\nWith a total of {sum([x.calorie_load for x in calorie_totals_by_elf[:3]])}")
