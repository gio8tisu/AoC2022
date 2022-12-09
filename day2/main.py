import sys
from typing import TextIO
from enum import Enum


class Result(Enum):
    WIN = 6
    DRAW = 3
    LOSS = 0


class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def play(self, other: "Choice") -> Result:
        """Return True if self beats other, False otherwise."""
        if self == other:
            return Result.DRAW
        if self == Choice.ROCK:
            return Result.WIN if other == Choice.SCISSORS else Result.LOSS
        if self == Choice.PAPER:
            return Result.WIN if other == Choice.ROCK else Result.LOSS
        if self == Choice.SCISSORS:
            return Result.WIN if other == Choice.PAPER else Result.LOSS
        raise ValueError(f"Unknown choice: {self}")


def main(strategy_guide: TextIO, part: int):
    if part == 1:
        rounds = read_strategy_guide_part_1(strategy_guide)
    elif part == 2:
        rounds = read_strategy_guide_part_2(strategy_guide)
    else:
        raise ValueError(f"Invalid part: {part}")
    round_scores = get_round_scores(rounds)
    print(sum(round_scores))


def read_strategy_guide_part_1(strategy_guide: TextIO) -> list[tuple[Choice, Choice]]:
    """Return list of player choices as per part 1 rules."""
    rounds = []
    for line in strategy_guide:
        oponent_choice, my_choice = line.strip("\n").split()
        rounds.append((guide_opponent_token_to_choice(
            oponent_choice), guide_my_token_to_choice(my_choice)))
    return rounds


def read_strategy_guide_part_2(strategy_guide: TextIO) -> list[tuple[Choice, Choice]]:
    """Return list of player choices as per part 2 rules."""
    rounds = []
    for line in strategy_guide:
        guide_oponent_choice, round_need = line.strip("\n").split()
        opponent_choice = guide_opponent_token_to_choice(guide_oponent_choice)
        rounds.append(
            (opponent_choice, guide_round_result_token_to_choice(round_need, opponent_choice)))
    return rounds


def guide_my_token_to_choice(token: str) -> Choice:
    if token == "X":
        return Choice.ROCK
    elif token == "Y":
        return Choice.PAPER
    elif token == "Z":
        return Choice.SCISSORS
    else:
        raise ValueError(f"Invalid token: {token}")


def guide_opponent_token_to_choice(token: str) -> Choice:
    if token == "A":
        return Choice.ROCK
    elif token == "B":
        return Choice.PAPER
    elif token == "C":
        return Choice.SCISSORS
    else:
        raise ValueError(f"Invalid token: {token}")


def guide_round_result_token_to_choice(token: str, opponent_choice: Choice) -> Choice:
    # Compute result for each choice and return the one that mathces desired result.
    choices = {choice.play(opponent_choice): choice for choice in Choice}
    if token == "X":    # Lose
        return choices[Result.LOSS]
    elif token == "Y":  # Draw
        return choices[Result.DRAW]
    elif token == "Z":  # Win
        return choices[Result.WIN]
    else:
        raise ValueError(f"Invalid token: {token}")


def get_round_scores(rounds: list[tuple[Choice, Choice]]) -> list[int]:
    return [get_round_score(round) for round in rounds]


def get_round_score(round: tuple[Choice, Choice]) -> int:
    opponent_choice, my_choice = round
    result = my_choice.play(opponent_choice)
    return result.value + my_choice.value


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    # File argument or stdin
    parser.add_argument("file", nargs="?",
                        type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--part", type=int, default=1,
                        help="Part 1 or 2 guide rules")

    args = parser.parse_args()
    main(args.file, args.part)
