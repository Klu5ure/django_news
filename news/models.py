from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    age = models.IntegerField()

    class Meta:
        db_table = 'student'
    
    # Django 会自动为每个模型提供一个 __str__ 方法
    def __str__(self):
        return self.name