from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=221)
    description = models.TextField()
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title