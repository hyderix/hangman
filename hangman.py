import get_dict


class Game:
    def __init__(self, word=None, tries=10):
        self.tries = tries
        self.initialtries = tries
        self.wrongletters = list()
        try:
            if word:
                self.word = str(word)
            else:
                self.word = self.pick_word()
        except Exception as e:
            print("Something went wrong({}).".format(e))
        self.revealed = ["_" for x in range(len(self.word))]
        
    def __del__(self):
        print(f"Bye from {type(self)}")
    def play(self):
        while True:
            if self.tries > 0:
                if "".join(self.revealed) == self.word:
                    print(f"Congratulations! The word was {self.word}, you did it in {self.initialtries-self.tries} tries")
                    return True
                
                print(f"Hangman: {''.join(self.revealed)}\nGuessed Letters: {''.join(self.wrongletters)}\nAttempts Left: {self.tries}\n-------------")
                user_input = input("Guess a letter: ").upper()
                print("-------------")
                if self.guess_letter(user_input):
                    print("Correct\n-------------")
                    continue
                else:
                    print("Incorrect\n-------------")
                    self.tries-=1
                    continue
            else:
                print(f"You've ran out of tries, the word was {self.word}.")
                return False

    def return_string(self):
        return "".join(self.revealed)
    def guess_letter(self, letter):
        for i in range(len(self.word)):
            if self.word[i] == letter.upper():
                self.reveal_letter(letter=letter)
                return True
        self.wrongletters.append(letter.upper())
        return False
    def reveal_letter(self, letter):
        for j in range(len(self.word)):
            if letter.upper() == self.word[j]:
                self.revealed[j] = self.word[j].upper()
    def pick_word(self):
        from random import choice
        '''Returns a word from the SOWPODS dictionary'''
        try:
            with open("dict.txt", "r") as dict_file:
                words = dict_file.read().split("\n")
        except:
            import get_dict
            self.pick_word()
        return choice(words)



