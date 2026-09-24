from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f'correcting "{word}" to "{corrected_word}"')

                return ' '.join(corrected_word)

    def run(self):
        print("\n ---spell checker---")

        while True:
            text = input('enter text to check for type "exit" to  quite : ')

            if text.lower() == 'exit':
                print('closing the program...')
                break
            corrected_text = self.correct_text(text)
            print(f'corrected text : {corrected_text}')

if __name__ == "__main__":
    SpellCheckerApp().run() 

print("thank you for using this !! ")