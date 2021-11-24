import hangman
import sys



if __name__ == "__main__":
    ARGV = sys.argv

    if len(ARGV) == 1:
        use_argv = False
    else:
        use_argv = True

    if not use_argv:
        hangman.Game().play()
    else:
        tries = int(ARGV[1])
        word = str(ARGV[2])

        hangman.Game(word, tries).play()
