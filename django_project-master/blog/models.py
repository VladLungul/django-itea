from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)

    def __str__(self):
        return f'S({self.first_name}, {self.last_name}, {self.email})'
    def __repr__(self):
        return self.__str__()

class Teacher(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    is_cool = models.BooleanField(default=False)
    email = models.EmailField(max_length=25)

    def __str__(self):
        return f'S({self.first_name}, {self.last_name}, {self.email})'

    def __repr__(self):
        return self.__str__()





