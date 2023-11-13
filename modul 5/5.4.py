import json

class Model:
    def save(self, filename):
        data = {}
        for attr, value in self.__dict__.items():
            if not callable(value):
                data[attr] = value

        with open(filename, 'w') as json_file:
            json.dump(data, json_file)

# Пример использования для класса Post (наследование от Model):
class Post(Model):
    def __init__(self, title, content, date_posted, author):
        self.title = title
        self.content = content
        self.date_posted = date_posted
        self.author = author

    def __str__(self):
        return self.title