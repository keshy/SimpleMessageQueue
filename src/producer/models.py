from django.db import models

# Create your models here.
''' contains the raw string to be captured in mongodb message queue'''
class Message(models.Model):
    msg = models.CharField(max_length=500)
    
    def __unicode__(self):
        return self.msg
