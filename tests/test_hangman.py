import unittest
from src.hangman import HangmanGame

class TestHangmanGame(unittest.TestCase):
    def setUp(self):
        self.game = HangmanGame()
        self.game.word = "TEST"
        self.game.current_display = "----"
        self.game.category = "Test Category"

    def test_correct_letter_guess(self):
        success, message = self.game.process_guess("T")
        self.assertTrue(success)
        self.assertEqual(self.game.current_display, "T--T")

    def test_incorrect_letter_guess(self):
        success, message = self.game.process_guess("X")
        self.assertFalse(success)
        self.assertEqual(self.game.turns_left, 4)

    def test_correct_word_guess(self):
        success, message = self.game.process_guess("TEST")
        self.assertTrue(success)
        self.assertTrue(self.game.is_game_won())

    def test_game_over_conditions(self):
        self.game.turns_left = 0
        self.assertTrue(self.game.is_game_over())

if __name__ == '__main__':
    unittest.main()