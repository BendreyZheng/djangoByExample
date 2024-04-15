from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE

# Create your models here.
class OpenJournalManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset()\
                    .filter(status=JournalProfile.Status.OPEN)


class JournalProfile(models.Model):

    class Status(models.TextChoices):
        OPEN = 'O', 'Open'
        CLOSED = 'C', 'Closed'
    
    user = models.OneToOneField(User, on_delete=CASCADE)
    name = models.CharField('Journal Name', max_length=100)
    ranking = models.IntegerField(blank=True, null=True)
    status = models.CharField('Submission status', choices=Status.choices, default=Status.CLOSED, blank=False, null=True, max_length=10)
    email = models.EmailField('Email', blank=True, null=True, max_length=200)
    description = models.TextField('Journal description', blank=True, null=True)
    submission_criteria = models.TextField('Submission criteria', blank=True, null=True)
    journal_cover = models.ImageField('Journal Cover Picture', null=True, blank=True)

    objects = models.Manager
    open = OpenJournalManager()

    class Meta:
        ordering = ['-ranking']
        indexes = [ # define databse indexes for the model
        models.Index(fields=['-ranking']),
        ]

    def __str__(self):
        return str(self.name)
  