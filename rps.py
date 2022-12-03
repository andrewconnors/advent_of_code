from typing import Dict, final

@final 
class RPSResult:
    WIN = 6
    DRAW = 3
    LOSS = 0

RPSHand: Dict[str, int] = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

StratTranslator: Dict[str, RPSResult] = {
    'X': RPSResult.LOSS,
    'Y': RPSResult.DRAW,
    'Z': RPSResult.WIN
}

def determine_winner(player: str, opponent: str):
    player_hand_val = RPSHand[player]
    opponent_hand_val = RPSHand[opponent]

    if player_hand_val == opponent_hand_val:
        return RPSResult.DRAW
    if(
        (player == 'X' and opponent == 'C') or 
        (player == 'Y' and opponent == 'A') or 
        (player == 'Z' and opponent == 'B')
    ):
        return RPSResult.WIN
    return RPSResult.LOSS

def determine_hand_to_satsify_strat(their_hand: str, desired_result: RPSResult) -> str:
    if desired_result == RPSResult.DRAW:
        return their_hand
    if desired_result == RPSResult.LOSS:
        return 'X' if their_hand == 'B' else ('Y' if their_hand == 'C' else 'Z')
    return 'X' if their_hand == 'C' else ('Y' if their_hand == 'A' else 'Z')

if __name__ == "__main__":
    total_round_1: int = 0
    total_round_2: int = 0
    with open('rps.txt', 'r') as input:
        for line in input:
            split_inputs = line.strip('\n').split(" ") # [their_hand, my_hand]

            #Challenge 1
            result: RPSResult = determine_winner(split_inputs[1], split_inputs[0])
            total_round_1 += RPSHand[split_inputs[1]] + result
            
            #Challenge 2
            hand_to_throw: str = determine_hand_to_satsify_strat(split_inputs[0], StratTranslator[split_inputs[1]])
            total_round_2 += RPSHand[hand_to_throw] + StratTranslator[split_inputs[1]]

    print(f"With this strategy, I will end up with {total_round_1} points. If I understood the elf correctly.")
    print(f"Turns out I didn't understand him correctly, I'll end up with {total_round_2} pts if I use their strategy.")

