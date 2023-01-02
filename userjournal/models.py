from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class JournalEntry(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    journal_entry = models.TextField()
    date_added = models.DateTimeField('Date Created', default=timezone.now)

    def get_absolute_url(self):
        return reverse('user-journal')
