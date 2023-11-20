import json


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

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
            
            
post = Post(title='Заголовок', content='Содержание', author='пользователь'))


post.save_to_json('post.json')