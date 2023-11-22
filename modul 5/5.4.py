import json


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return self.title

    def save_to_json(self, file_path):
        post_data = {
            'title': self.title,
            'content': self.content,
            'author': self.author,
        }

        with open(file_path, 'w') as json_file:
            json.dump(post_data, json_file)
            
            
post = Post(title='Заголовок', content='Содержание', author='пользователь')


post.save_to_json('post.json')

with open('post.json', 'r') as json_file:
    fcc_data = json.load(json_file)

print(fcc_data)
