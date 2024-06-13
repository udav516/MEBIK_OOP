import string


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print_letters(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return "The quick brown fox jumps over the lazy dog."


eng_alphabet = EngAlphabet()
eng_alphabet.print_letters()
print(eng_alphabet.letters_num())
print(eng_alphabet.is_en_letter('F'))
print(eng_alphabet.is_en_letter('Щ'))
print(EngAlphabet.example())
