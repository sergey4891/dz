import json

class Model:
    def save(self, filename):
        # Создаем словарь со всеми атрибутами объекта
        obj_dict = {}
        for field_name in self.__dict__:
            obj_dict[field_name] = getattr(self, field_name)

        # Записываем словарь в файл JSON
        with open(filename, 'w') as json_file:
            json.dump(obj_dict, json_file, indent=4)


class Post(models.Model, Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


post = Post.objects.get(pk=1)  # Получаем объект Post из базы данных
post.save('post.json')  # Сохраняем его в файл 'post.json'