from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField('date')
    
    def __str__(self):
        return self.name

class Attend(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    did_lunch = models.IntegerField(default=0)
    date = models.DateTimeField('date')

    def __str__(self):
        return str(self.users) + ' [' + str(self.did_lunch) + '] '