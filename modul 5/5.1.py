class StringVar:
    def  __init__(self):
        self.str = ""
        pass

    def set(self, word):
        self.str = word

    def get(self):
        return self.str


stringvar = StringVar()
stringvar.set("Тестовая строка")
print(stringvar.get())