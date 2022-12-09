import unittest

from main import Choice, get_round_score, Result, guide_round_result_token_to_choice


class TestChoicePlay(unittest.TestCase):

    def test_rock_play_rock(self):
        self.assertEqual(Choice.ROCK.play(Choice.ROCK), Result.DRAW)

    def test_paper_play_paper(self):
        self.assertEqual(Choice.PAPER.play(Choice.PAPER), Result.DRAW)

    def test_scissors_play_scissors(self):
        self.assertEqual(Choice.SCISSORS.play(Choice.SCISSORS), Result.DRAW)

    def test_rock_play_scissors(self):
        self.assertEqual(Choice.ROCK.play(Choice.SCISSORS), Result.WIN)

    def test_paper_play_rock(self):
        self.assertEqual(Choice.PAPER.play(Choice.ROCK), Result.WIN)

    def test_scissors_play_paper(self):
        self.assertEqual(Choice.SCISSORS.play(Choice.PAPER), Result.WIN)

    def test_scissors_play_rock(self):
        self.assertEqual(Choice.SCISSORS.play(Choice.ROCK), Result.LOSS)

    def test_rock_play_paper(self):
        self.assertEqual(Choice.ROCK.play(Choice.PAPER), Result.LOSS)

    def test_paper_play_scissors(self):
        self.assertEqual(Choice.PAPER.play(Choice.SCISSORS), Result.LOSS)


class TestRoundScore(unittest.TestCase):

    def test_round1_score(self):
        """
        In the first round, your opponent will choose Rock (A), and you
        should choose Paper (Y). This ends in a win for you with a score of 8
        (2 because you chose Paper + 6 because you won).
        """
        score = get_round_score((Choice.ROCK, Choice.PAPER))
        self.assertEqual(score, 8)

    def test_round2_score(self):
        """
        In the second round, your opponent will choose Paper (B), and you
        should choose Rock (X). This ends in a loss for you with a score of 1
        (1 + 0).
        """
        score = get_round_score((Choice.PAPER, Choice.ROCK))
        self.assertEqual(score, 1)

    def test_round3_score(self):
        """
        The third round is a draw with both players choosing Scissors,
        giving you a score of 3 + 3 = 6.
        """
        score = get_round_score((Choice.SCISSORS, Choice.SCISSORS))
        self.assertEqual(score, 6)


class TestGuideRoundNeedToChoice(unittest.TestCase):
    def test_example_1(self):
        """
        In the first round, your opponent will choose Rock (A), and you need
        the round to end in a draw (Y), so you also choose Rock.
        """
        choice = guide_round_result_token_to_choice("Y", Choice.ROCK)
        self.assertEqual(choice, Choice.ROCK)

    def test_example_2(self):
        """
        In the second round, your opponent will choose Paper (B), and you
        choose Rock so you lose (X). """
        choice = guide_round_result_token_to_choice("X", Choice.PAPER)
        self.assertEqual(choice, Choice.ROCK)

    def test_example_3(self):
        """
        In the third round, you will defeat (Z) your opponent's Scissors with Rock.
        """
        choice = guide_round_result_token_to_choice("Z", Choice.SCISSORS)
        self.assertEqual(choice, Choice.ROCK)


if __name__ == "__main__":
    unittest.main()
