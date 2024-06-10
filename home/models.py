from django.db import models
from datetime import date
from django.utils import timezone
import uuid

class Joke(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(default=date.today, editable=False)
    joke = models.CharField(max_length=100)
    category = models.CharField(max_length=30)
    from_user = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id) + ': ' + self.joke + '___________' + self.category + '___________' + self.from_user + '___________' + str(self.created_at)
    

class ReportedJoke(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    joke_id = models.UUIDField(editable=False)
    ReportCategory = models.CharField(max_length=30, editable=False)
    ReportTextField = models.CharField(max_length=50, editable=False, default='None')
    joke = models.CharField(max_length=100, editable=False)
    from_user = models.CharField(max_length=20, editable=False)
    
    def __str__(self):
        return str(self.id) + ': Joke_Id: ' + str(self.joke_id) + '___________' + 'Report Category: ' + self.ReportCategory + '___________' + 'Joke created by : ' + self.from_user


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sended_on = models.DateTimeField(auto_now_add=True, editable=False)
    header = models.CharField(max_length=100)
    content = models.CharField(max_length=400)
    for_user = models.CharField(max_length=40, blank=True, default='')

    def __str__(self):
        return str(self.for_user) + ': ' + self.header