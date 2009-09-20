from django.db import models

class Strip(models.Model):

    # the database fields
    title    = models.CharField(max_length=256)
    alt_text = models.CharField(max_length=256)
    path     = models.CharField(max_length=512)
    sub_date = models.DateTimeField('submission date')

    def __unicode__(self):
        return self.title
