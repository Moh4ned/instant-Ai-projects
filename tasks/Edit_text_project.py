class Edittext:
    def __init__(self, text="Honda"):
        self.text = text

    def set_text(self, gettext):
        self.text = gettext

    def get_text(self):
        return self.text

    @staticmethod
    def rem_repeated(self):
        if len(self.text) == 1:
            return self.text

        if self.text[0] == self.text[1]:
            return self.rem_repeated(self.text[1:])

        return self.text[0] + self.rem_repeated(self.text[1:])


class Texts(Edittext):
    def __init__(self, text="Honda"):
        super().__init__(text)

    @classmethod
    def revers(cls,rev_text):
        return cls(rev_text[::-1])

    def upper_text(self):
        return self.text.upper()

    def lower_text(self):
        return self.text.lower()

    def snake_case(self):
        words = self.text
        snake_case = words.replace(" ", "_").lower()
        return snake_case

    def camel_case(self):
        words = self.text.split()
        camel_case = words[0].lower() + ''.join(word.title() for word in words[1:])
        return camel_case

text1=Texts("mohand magdy abdelrauf")
print(text1.snake_case())
print(text1.camel_case())
print(text1.lower_text())
print(text1.upper_text())



