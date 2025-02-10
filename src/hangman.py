import random
import time
import sys
from typing import Tuple, List

from .ascii_art import HANGMAN_STATES
from .word_bank import WORD_CATEGORIES

class HangmanGame:
    def __init__(self):
        self.player_name = ""
        self.word = ""
        self.category = ""
        self.guessed_letters = []
        self.guessed_words = []
        self.turns_left = 5
        self.current_display = ""
        self.wrong_guesses = 0

    def initialize_game(self) -> None:
        """Initialize a new game with a random word."""
        category = random.choice(list(WORD_CATEGORIES.keys()))
        word = random.choice(WORD_CATEGORIES[category])
        self.word = word.upper()
        self.category = category
        self.current_display = '-' * len(self.word)
        self.guessed_letters = []
        self.guessed_words = []
        self.turns_left = 5
        self.wrong_guesses = 0

    def display_game_state(self) -> None:
        """Display current game state."""
        print(f"\nTotal chances left: {self.turns_left}")
        print(f"Word length: {len(self.word)}")
        print(' '.join(self.current_display))
        print(f"HINT - {self.category}")

    def process_guess(self, guess: str) -> Tuple[bool, str]:
        """Process a player's guess and return game status."""
        guess = guess.upper()
        
        if len(guess) == 1:  # Single letter guess
            if guess in self.guessed_letters:
                return False, "You have already guessed this letter"
            
            self.guessed_letters.append(guess)
            if guess in self.word:
                new_display = list(self.current_display)
                for i, letter in enumerate(self.word):
                    if letter == guess:
                        new_display[i] = guess
                self.current_display = ''.join(new_display)
                return True, "Good guess!"
            else:
                self.wrong_guesses += 1
                self.turns_left -= 1
                return False, f"Wrong guess! {self.turns_left} chances left"
                
        elif len(guess) == len(self.word):  # Whole word guess
            if guess in self.guessed_words:
                return False, "You have already guessed this word"
            
            self.guessed_words.append(guess)
            if guess == self.word:
                self.current_display = self.word
                return True, "Correct word!"
            else:
                self.wrong_guesses += 1
                self.turns_left -= 1
                return False, f"Wrong word! {self.turns_left} chances left"
        
        return False, "Invalid guess"

    def is_game_won(self) -> bool:
        """Check if the game is won."""
        return self.current_display == self.word

    def is_game_over(self) -> bool:
        """Check if the game is over."""
        return self.turns_left == 0 or self.is_game_won()

def main():
    game = HangmanGame()
    
    # Get player name
    game.player_name = input("Hey, what's your name? ").upper()
    print(f'Hello {game.player_name}! Welcome to HANGMAN game!\n')
    
    while True:
        choice = input("Type 'y' to play the game or 'n' to exit: ").lower()
        if choice == 'n':
            print(f"\nHope we'll meet soon {game.player_name} :)")
            sys.exit()
        elif choice == 'y':
            break
        print("Invalid input. Please type 'y' or 'n'")

    # Main game loop
    while True:
        game.initialize_game()
        game.display_game_state()
        
        while not game.is_game_over():
            guess = input("\nGUESS A LETTER OR THE WORD: ")
            success, message = game.process_guess(guess)
            print(message)
            
            if game.wrong_guesses > 0:
                print(HANGMAN_STATES[game.wrong_guesses])
            
            if not game.is_game_over():
                game.display_game_state()
        
        if game.is_game_won():
            print(f"\nHURRAYY!!! You saved the hangman! :) Good Job {game.player_name}, you can be a detective")
        else:
            print(f"\nOh no.. BETTER LUCK NEXT TIME. The word was: {game.word}")
            
        if input("\nWant to play again? (Y/N): ").upper() != 'Y':
            break
    
    print("Thank you for playing ;)")

if __name__ == "__main__":
    main()