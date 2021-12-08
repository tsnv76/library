from django.db import models

# [Client] -> [Router/URL] -> [View] -> [Serializer] -> [Model]


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()
    email = models.EmailField('email address', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

