from django.db import models

class Strip(models.Model):

    # the database fields
    title    = models.CharField(max_length=256)
    alt_text = models.CharField(max_length=256)
    sub_date = models.DateField('submission date')
    strip    = models.FileField(upload_to='strips')

    def __unicode__(self):
        return 'Strip #%s' % self.id
