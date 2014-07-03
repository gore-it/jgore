from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    publication_date = models.DateTimeField(auto_created=True, blank=True, null=True)

    def __unicode__(self):
        return self.title
