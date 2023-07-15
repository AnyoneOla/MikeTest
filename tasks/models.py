from django.db import models


# Create your models here.

# class Status(models.TextChoices):
#     UNSTARTED = 'u', "Not started yet"
#     ONGOING = 'o', "Ongoing"
#     FINISHED = 'f', "Finished"


# class Task(models.Model):
#     name = models.CharField(verbose_name="Task name", max_length=65, unique=True)
#     status = models.CharField(verbose_name="Task status", max_length=1, choices=Status.choices)


class Songs(models.TextChoices):
    A = 'Dildara', "Dildara"
    B = 'Perfect', "Perfect"
    C = 'Angel', "Angel"
    D = 'I need You', "I Need You"
    
class User_Request(models.Model):
    name = models.CharField(verbose_name="Name", max_length=500)
    contact = models.IntegerField(verbose_name="Phone", unique=True, primary_key=True)
    song = models.CharField(verbose_name="Song", max_length=100, choices=Songs.choices)

    def __str__(self):
        return self.name
