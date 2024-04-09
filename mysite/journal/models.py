from django.db import models

# Create your models here.
class Post(models.Model):
  STATUS = (
        ('O', 'Open'),
        ('C', 'Closed'),
    )
  user = models.OneToOneField(User, on_delete=CASCADE, related_name='jprofile')
  status = models.CharField('Submission status', choices=STATUS, blank=False, null=True, max_length=10)
  email = models.EmailField('Email', blank=True, null=True, max_length=200)
  description = models.TextField('Journal description', blank=True, null=True)
  submission_criteria = models.TextField('Submission criteria', blank=True, null=True)
  journal_cover = models.ImageField('Journal Cover Picture',
                                      storage=GoogleCloudStorage(bucket_name=settings.GCS_USER_BUCKET_NAME),
                                      upload_to=user_directory_journal_cover, null=True, blank=True)

  def __str__(self):
      return str(self.user)
  