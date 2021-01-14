import hangman
import sys

def play_hangman(tries, word=None):
    game = hangman.Game(word, tries).play()
    return game



if __name__ == "__main__":
    ARGV = sys.argv()

    if ARGV == [__file__]:
        use_argv = False
    else:
        use_argv = True

    if not use_argv:
        tries = input("Enter the number of tries: ")
        word = input("Enter the word to use: ")
    else:
        tries = ARGV[1]
        word = ARGV[2]

    play_hangman(tries, word)
