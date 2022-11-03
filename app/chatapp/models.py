from django.db import models

# Create your models here.


class Rooms(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Chats(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
