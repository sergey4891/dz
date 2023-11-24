import json


class Post:
    def __init__(self, *args, **kwargs):
        self.data = kwargs

    def save_to_json(self, file_path):

        with open(file_path, 'w') as json_file:
            json.dump(self.data, json_file)
            
            
post = Post(title='Заголовок', content='Содержание', author='пользователь')


post.save_to_json('post.json')

with open('post.json', 'r') as json_file:
    fcc_data = json.load(json_file)

print(fcc_data)
